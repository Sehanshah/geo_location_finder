# Using Map Quest Free API Services
# Geo Location documentaion link - https://developer.mapquest.com/documentation/geocoding-api/address/get/
# property used to get lat and lon - https://developer.mapquest.com/documentation/geocoding-api/address/get/#response_field-displayLatLng
# To know transaction history. Visit - https://developer.mapquest.com/user/me/transaction-report


API_KEY = 'Go9GJDxsz4acCaXFxSuwHreA9U54GCMQ'

def get_geo_info(address):
    return f'http://www.mapquestapi.com/geocoding/v1/address?key={API_KEY}&location={address}'