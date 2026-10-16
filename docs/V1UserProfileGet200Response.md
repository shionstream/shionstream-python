# V1UserProfileGet200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** |  | 
**data** | [**V1UserProfileGet200ResponseData**](V1UserProfileGet200ResponseData.md) |  | 

## Example

```python
from shionstream_sdk.models.v1_user_profile_get200_response import V1UserProfileGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of V1UserProfileGet200Response from a JSON string
v1_user_profile_get200_response_instance = V1UserProfileGet200Response.from_json(json)
# print the JSON string representation of the object
print(V1UserProfileGet200Response.to_json())

# convert the object into a dict
v1_user_profile_get200_response_dict = v1_user_profile_get200_response_instance.to_dict()
# create an instance of V1UserProfileGet200Response from a dict
v1_user_profile_get200_response_from_dict = V1UserProfileGet200Response.from_dict(v1_user_profile_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


