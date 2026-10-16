# V1UserHistoryGet200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** |  | 
**data** | [**List[V1UserHistoryGet200ResponseDataInner]**](V1UserHistoryGet200ResponseDataInner.md) |  | 

## Example

```python
from shionstream_sdk.models.v1_user_history_get200_response import V1UserHistoryGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of V1UserHistoryGet200Response from a JSON string
v1_user_history_get200_response_instance = V1UserHistoryGet200Response.from_json(json)
# print the JSON string representation of the object
print(V1UserHistoryGet200Response.to_json())

# convert the object into a dict
v1_user_history_get200_response_dict = v1_user_history_get200_response_instance.to_dict()
# create an instance of V1UserHistoryGet200Response from a dict
v1_user_history_get200_response_from_dict = V1UserHistoryGet200Response.from_dict(v1_user_history_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


