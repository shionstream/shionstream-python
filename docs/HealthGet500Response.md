# HealthGet500Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | 
**timestamp** | **str** |  | 
**database** | **str** |  | 
**error** | **str** |  | [optional] 

## Example

```python
from shionstream_sdk.models.health_get500_response import HealthGet500Response

# TODO update the JSON string below
json = "{}"
# create an instance of HealthGet500Response from a JSON string
health_get500_response_instance = HealthGet500Response.from_json(json)
# print the JSON string representation of the object
print(HealthGet500Response.to_json())

# convert the object into a dict
health_get500_response_dict = health_get500_response_instance.to_dict()
# create an instance of HealthGet500Response from a dict
health_get500_response_from_dict = HealthGet500Response.from_dict(health_get500_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


