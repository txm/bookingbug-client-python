import bookingbug.business
import bookingbug.resource


business_params = dict( {
    "address1":"travelBed",
    "address2":"Pembroke Road",
    "postcode":"BS1 2NN",
    "address3":"Bristol",
    "address4":"",
    "country":"United Kingdom",
    "email":"andy@travelbed.com",
    "name":"travelBed",
    "description":"travelBed B&B",
    "template_id":"1",
    "id":"1",
    "role":"1"
} )

business_config = dict( {
    "uri":'http://staging.booking-bug.com/api/company/',
    "htuser":"XXX",
    "htpass":"XXX",
    "debug":None,
} )

create_business_json = bookingbug.business.get_json(business_params)
business_d = bookingbug.business.create( json = create_business_json, config = business_config )
print business_d.contents


resource_params = dict( {
    "company_id":business_d.contents['id'],
    "name":"Red Room",
    "description":"The Red Bedroom"
} )

resource_config = dict( {
    "uri":'http://staging.booking-bug.com/api/resource/',
    "htuser":"XXX",
    "htpass":"XXX",
    "debug":None,
} )

create_resource_json = bookingbug.resource.get_json(resource_params)
resource_d = bookingbug.resource.create( json = create_resource_json, config = resource_config )
print resource_d.contents
