#! /usr/bin/env python

if __name__ == '__main__':
    print "unit testing required"
    exit(1)


import sys
import pycurl
import fileinput
import pprint
import simplejson as json


class CreateCompany:
    def __init__(self):
        self.contents = ''
        self.json = ''

    def body_callback(self, buf):
        self.json = self.json + buf

    def convert_json(self):
        self.contents = json.loads(self.json)


def progress(download_t, download_d, upload_t, upload_d):
    print "Total to download", download_t
    print "Total downloaded", download_d
    print "Total to upload", upload_t
    print "Total uploaded", upload_d


def test(debug_type, debug_msg):
    print "debug(%d): %s" % (debug_type, debug_msg)


def create(json,config):

    if json == None:
        print >>sys.stderr, "json is not defined"
        exit(111)

    if config['debug']:
        print >>sys.stderr, 'Create new BookingBug Company', pycurl.version

    company_o = CreateCompany()
    curl_o = pycurl.Curl()
    curl_o.setopt(curl_o.URL, config['uri'])
    curl_o.setopt(pycurl.HTTPHEADER, ["Accept:application/json", "Content-type:application/json"])
    curl_o.setopt(pycurl.USERPWD , "%s:%s" % (config['htuser'], config['htpass']) )
    curl_o.setopt(pycurl.POST, 1)
    curl_o.setopt(pycurl.POSTFIELDS, json)
    curl_o.setopt(curl_o.WRITEFUNCTION, company_o.body_callback)

    if config['debug']:
        curl_o.setopt(curl_o.PROGRESSFUNCTION, progress)
        curl_o.setopt(pycurl.DEBUGFUNCTION, test)
        curl_o.setopt(curl_o.NOPROGRESS, 0)
        curl_o.setopt(pycurl.VERBOSE, 1)

    curl_o.perform()

    if config['debug']:
        print curl_o.getinfo(pycurl.HTTP_CODE), curl_o.getinfo(pycurl.EFFECTIVE_URL)

    curl_o.close()

    company_o.convert_json()

    return company_o


def get_json(params_d):
    #pp = pprint.PrettyPrinter(indent=4)
    #pp.pprint(params_d)

    record_d = dict(
{
  "record":{
    "address":{
      "address1":params_d['address1'],
      "address2":params_d['address2'],
      "postcode":params_d['postcode'],
      "address3":params_d['address3'],
      "address4":params_d['address4'],
      "country":params_d['country'],
      "email":params_d['email'],
    },
    "name":params_d['name'],
    "description":params_d['description'],
    "template_id":params_d['template_id'],
    "administrators":{
      "user1":{
        "user":{
          "id":params_d['id'],
        },
        "role":params_d['role'],
      }
    }
  }
}
    )

    json_record_s = json.dumps( record_d, separators=(',',':') )

    return json_record_s
