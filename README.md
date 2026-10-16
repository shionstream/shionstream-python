# shionstream-sdk
Modular anime streaming and metadata API built with Hono on Cloudflare Workers.

This Python package is automatically generated for ShionStream API using OpenAPI specification.

- API version: 1.0.0
- Package version: 1.0.0
- Generator version: 7.26.0
- Build package: org.openapitools.codegen.languages.PythonClientCodegen
For more information, please visit [https://gox.my.id](https://gox.my.id)

## Requirements.

Python 3.10+

Packaging uses standard `[project]` metadata and `[dependency-groups]` (PEP 621/735).
Install the package with `python -m pip install .`; install development dependencies
with Poetry 2.2 or newer using `poetry install`, or pip 25.1 or newer using
`python -m pip install --group dev`. The latter installs the group, not the package.

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/shionstream/shionstream-python.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/shionstream/shionstream-python.git`)

Then import the package:
```python
import shionstream_sdk
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import shionstream_sdk
```

### Tests

Execute `pytest` to run the tests.

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python

import shionstream_sdk
from shionstream_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.gox.my.id
# See configuration.py for a list of all supported configuration parameters.
configuration = shionstream_sdk.Configuration(
    host = "https://api.gox.my.id"
)



# Enter a context with an instance of the API client
with shionstream_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = shionstream_sdk.AnimeApi(api_client)
    page = '1' # str |  (optional) (default to '1')
    limit = '20' # str |  (optional) (default to '20')
    search = 'search_example' # str |  (optional)
    type = 'type_example' # str |  (optional)
    status = 'status_example' # str |  (optional)
    genre = 'genre_example' # str |  (optional)
    season = 'season_example' # str |  (optional)
    year = 'year_example' # str |  (optional)
    sort = 'latest' # str |  (optional) (default to 'latest')

    try:
        # List Anime Catalog
        api_response = api_instance.v1_anime_get(page=page, limit=limit, search=search, type=type, status=status, genre=genre, season=season, year=year, sort=sort)
        print("The response of AnimeApi->v1_anime_get:\n")
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AnimeApi->v1_anime_get: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *https://api.gox.my.id*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AnimeApi* | [**v1_anime_get**](docs/AnimeApi.md#v1_anime_get) | **GET** /v1/anime | List Anime Catalog
*AnimeApi* | [**v1_anime_slug_get**](docs/AnimeApi.md#v1_anime_slug_get) | **GET** /v1/anime/{slug} | Get Anime Details by Slug
*CommentsApi* | [**v1_comments_get**](docs/CommentsApi.md#v1_comments_get) | **GET** /v1/comments | Get Episode Comments
*CommentsApi* | [**v1_comments_id_like_post**](docs/CommentsApi.md#v1_comments_id_like_post) | **POST** /v1/comments/{id}/like | Like or Dislike Comment
*CommentsApi* | [**v1_comments_id_report_post**](docs/CommentsApi.md#v1_comments_id_report_post) | **POST** /v1/comments/{id}/report | Report Comment
*CommentsApi* | [**v1_comments_post**](docs/CommentsApi.md#v1_comments_post) | **POST** /v1/comments | Create Comment
*DashboardApi* | [**v1_dashboard_anime_get**](docs/DashboardApi.md#v1_dashboard_anime_get) | **GET** /v1/dashboard/anime | Get Administrative Anime List
*DashboardApi* | [**v1_dashboard_categories_get**](docs/DashboardApi.md#v1_dashboard_categories_get) | **GET** /v1/dashboard/categories | Get Category &amp; Genre Distributions
*DashboardApi* | [**v1_dashboard_episodes_get**](docs/DashboardApi.md#v1_dashboard_episodes_get) | **GET** /v1/dashboard/episodes | Get Administrative Episodes List
*DashboardApi* | [**v1_dashboard_moderation_get**](docs/DashboardApi.md#v1_dashboard_moderation_get) | **GET** /v1/dashboard/moderation | Get Comment Moderation Reports
*DashboardApi* | [**v1_dashboard_moderation_id_patch**](docs/DashboardApi.md#v1_dashboard_moderation_id_patch) | **PATCH** /v1/dashboard/moderation/{id} | Resolve or Dismiss Moderation Report
*DashboardApi* | [**v1_dashboard_overview_get**](docs/DashboardApi.md#v1_dashboard_overview_get) | **GET** /v1/dashboard/overview | Get Dashboard Overview
*DashboardApi* | [**v1_dashboard_roles_get**](docs/DashboardApi.md#v1_dashboard_roles_get) | **GET** /v1/dashboard/roles | Get System Roles &amp; Permissions
*DashboardApi* | [**v1_dashboard_seasons_get**](docs/DashboardApi.md#v1_dashboard_seasons_get) | **GET** /v1/dashboard/seasons | Get Seasonal Broadcast Distributions
*DashboardApi* | [**v1_dashboard_stats_get**](docs/DashboardApi.md#v1_dashboard_stats_get) | **GET** /v1/dashboard/stats | Get Platform Stats
*DashboardApi* | [**v1_dashboard_users_get**](docs/DashboardApi.md#v1_dashboard_users_get) | **GET** /v1/dashboard/users | Get Users Directory (Admin Only)
*EpisodesApi* | [**v1_anime_slug_episodes_get**](docs/EpisodesApi.md#v1_anime_slug_episodes_get) | **GET** /v1/anime/{slug}/episodes | List Episodes by Anime Slug
*EpisodesApi* | [**v1_episodes_id_stream_get**](docs/EpisodesApi.md#v1_episodes_id_stream_get) | **GET** /v1/episodes/{id}/stream | Get Episode Stream Sources
*SampleApi* | [**v1_protected_sample_get**](docs/SampleApi.md#v1_protected_sample_get) | **GET** /v1/protected/sample | Protected Sample Endpoint
*SystemApi* | [**health_get**](docs/SystemApi.md#health_get) | **GET** /health | Health Check
*UploadApi* | [**v1_upload_hls_post**](docs/UploadApi.md#v1_upload_hls_post) | **POST** /v1/upload/hls | Upload HLS Package to Cloudflare R2
*UploadApi* | [**v1_upload_image_post**](docs/UploadApi.md#v1_upload_image_post) | **POST** /v1/upload/image | Upload Image to Cloudflare R2
*UserApi* | [**v1_user_history_delete**](docs/UserApi.md#v1_user_history_delete) | **DELETE** /v1/user/history | Clear All History
*UserApi* | [**v1_user_history_get**](docs/UserApi.md#v1_user_history_get) | **GET** /v1/user/history | Get Watch History
*UserApi* | [**v1_user_history_id_delete**](docs/UserApi.md#v1_user_history_id_delete) | **DELETE** /v1/user/history/{id} | Delete History Item
*UserApi* | [**v1_user_history_post**](docs/UserApi.md#v1_user_history_post) | **POST** /v1/user/history | Record Playback Progress
*UserApi* | [**v1_user_profile_get**](docs/UserApi.md#v1_user_profile_get) | **GET** /v1/user/profile | Get User Profile
*UserApi* | [**v1_user_settings_get**](docs/UserApi.md#v1_user_settings_get) | **GET** /v1/user/settings | Get User Settings
*UserApi* | [**v1_user_settings_patch**](docs/UserApi.md#v1_user_settings_patch) | **PATCH** /v1/user/settings | Update User Settings
*UserApi* | [**v1_user_watchlist_anime_id_delete**](docs/UserApi.md#v1_user_watchlist_anime_id_delete) | **DELETE** /v1/user/watchlist/{animeId} | Remove from Watchlist
*UserApi* | [**v1_user_watchlist_anime_id_patch**](docs/UserApi.md#v1_user_watchlist_anime_id_patch) | **PATCH** /v1/user/watchlist/{animeId} | Update Watchlist Entry
*UserApi* | [**v1_user_watchlist_get**](docs/UserApi.md#v1_user_watchlist_get) | **GET** /v1/user/watchlist | Get User Watchlist
*UserApi* | [**v1_user_watchlist_post**](docs/UserApi.md#v1_user_watchlist_post) | **POST** /v1/user/watchlist | Add to Watchlist


## Documentation For Models

 - [HealthGet200Response](docs/HealthGet200Response.md)
 - [HealthGet500Response](docs/HealthGet500Response.md)
 - [V1AnimeGet200Response](docs/V1AnimeGet200Response.md)
 - [V1AnimeGet200ResponseDataInner](docs/V1AnimeGet200ResponseDataInner.md)
 - [V1AnimeGet200ResponsePagination](docs/V1AnimeGet200ResponsePagination.md)
 - [V1AnimeSlugEpisodesGet200Response](docs/V1AnimeSlugEpisodesGet200Response.md)
 - [V1AnimeSlugEpisodesGet200ResponseAnime](docs/V1AnimeSlugEpisodesGet200ResponseAnime.md)
 - [V1AnimeSlugEpisodesGet200ResponseDataInner](docs/V1AnimeSlugEpisodesGet200ResponseDataInner.md)
 - [V1AnimeSlugGet200Response](docs/V1AnimeSlugGet200Response.md)
 - [V1AnimeSlugGet200ResponseData](docs/V1AnimeSlugGet200ResponseData.md)
 - [V1AnimeSlugGet200ResponseDataGenresInner](docs/V1AnimeSlugGet200ResponseDataGenresInner.md)
 - [V1AnimeSlugGet200ResponseDataSchedule](docs/V1AnimeSlugGet200ResponseDataSchedule.md)
 - [V1AnimeSlugGet200ResponseDataTrendingStats](docs/V1AnimeSlugGet200ResponseDataTrendingStats.md)
 - [V1CommentsGet200Response](docs/V1CommentsGet200Response.md)
 - [V1CommentsGet200ResponseDataInner](docs/V1CommentsGet200ResponseDataInner.md)
 - [V1CommentsIdLikePost200Response](docs/V1CommentsIdLikePost200Response.md)
 - [V1CommentsIdLikePostRequest](docs/V1CommentsIdLikePostRequest.md)
 - [V1CommentsIdReportPostRequest](docs/V1CommentsIdReportPostRequest.md)
 - [V1CommentsPost201Response](docs/V1CommentsPost201Response.md)
 - [V1CommentsPostRequest](docs/V1CommentsPostRequest.md)
 - [V1DashboardAnimeGet200Response](docs/V1DashboardAnimeGet200Response.md)
 - [V1DashboardCategoriesGet200Response](docs/V1DashboardCategoriesGet200Response.md)
 - [V1DashboardCategoriesGet200ResponseCategoriesInner](docs/V1DashboardCategoriesGet200ResponseCategoriesInner.md)
 - [V1DashboardCategoriesGet200ResponseGenresInner](docs/V1DashboardCategoriesGet200ResponseGenresInner.md)
 - [V1DashboardEpisodesGet200Response](docs/V1DashboardEpisodesGet200Response.md)
 - [V1DashboardModerationGet200Response](docs/V1DashboardModerationGet200Response.md)
 - [V1DashboardModerationGet200ResponseReportsInner](docs/V1DashboardModerationGet200ResponseReportsInner.md)
 - [V1DashboardModerationGet200ResponseReportsInnerAuthor](docs/V1DashboardModerationGet200ResponseReportsInnerAuthor.md)
 - [V1DashboardModerationGet200ResponseReportsInnerReporter](docs/V1DashboardModerationGet200ResponseReportsInnerReporter.md)
 - [V1DashboardModerationIdPatchRequest](docs/V1DashboardModerationIdPatchRequest.md)
 - [V1DashboardOverviewGet200Response](docs/V1DashboardOverviewGet200Response.md)
 - [V1DashboardOverviewGet200ResponseNotificationsInner](docs/V1DashboardOverviewGet200ResponseNotificationsInner.md)
 - [V1DashboardOverviewGet200ResponseRecentActivitiesInner](docs/V1DashboardOverviewGet200ResponseRecentActivitiesInner.md)
 - [V1DashboardOverviewGet200ResponseTrafficDataInner](docs/V1DashboardOverviewGet200ResponseTrafficDataInner.md)
 - [V1DashboardRolesGet200Response](docs/V1DashboardRolesGet200Response.md)
 - [V1DashboardRolesGet200ResponseRolesInner](docs/V1DashboardRolesGet200ResponseRolesInner.md)
 - [V1DashboardSeasonsGet200Response](docs/V1DashboardSeasonsGet200Response.md)
 - [V1DashboardSeasonsGet200ResponseSeasonsInner](docs/V1DashboardSeasonsGet200ResponseSeasonsInner.md)
 - [V1DashboardStatsGet200Response](docs/V1DashboardStatsGet200Response.md)
 - [V1DashboardStatsGet200ResponseStats](docs/V1DashboardStatsGet200ResponseStats.md)
 - [V1DashboardUsersGet200Response](docs/V1DashboardUsersGet200Response.md)
 - [V1DashboardUsersGet200ResponseUsersInner](docs/V1DashboardUsersGet200ResponseUsersInner.md)
 - [V1EpisodesIdStreamGet200Response](docs/V1EpisodesIdStreamGet200Response.md)
 - [V1EpisodesIdStreamGet200ResponseAudioInner](docs/V1EpisodesIdStreamGet200ResponseAudioInner.md)
 - [V1EpisodesIdStreamGet200ResponseEpisode](docs/V1EpisodesIdStreamGet200ResponseEpisode.md)
 - [V1EpisodesIdStreamGet200ResponseSourcesInner](docs/V1EpisodesIdStreamGet200ResponseSourcesInner.md)
 - [V1EpisodesIdStreamGet200ResponseSubtitlesInner](docs/V1EpisodesIdStreamGet200ResponseSubtitlesInner.md)
 - [V1ProtectedSampleGet200Response](docs/V1ProtectedSampleGet200Response.md)
 - [V1ProtectedSampleGet200ResponseUser](docs/V1ProtectedSampleGet200ResponseUser.md)
 - [V1ProtectedSampleGet401Response](docs/V1ProtectedSampleGet401Response.md)
 - [V1UploadHlsPost200Response](docs/V1UploadHlsPost200Response.md)
 - [V1UploadHlsPost200ResponseData](docs/V1UploadHlsPost200ResponseData.md)
 - [V1UploadImagePost200Response](docs/V1UploadImagePost200Response.md)
 - [V1UploadImagePost200ResponseData](docs/V1UploadImagePost200ResponseData.md)
 - [V1UserHistoryGet200Response](docs/V1UserHistoryGet200Response.md)
 - [V1UserHistoryGet200ResponseDataInner](docs/V1UserHistoryGet200ResponseDataInner.md)
 - [V1UserHistoryPostRequest](docs/V1UserHistoryPostRequest.md)
 - [V1UserProfileGet200Response](docs/V1UserProfileGet200Response.md)
 - [V1UserProfileGet200ResponseData](docs/V1UserProfileGet200ResponseData.md)
 - [V1UserProfileGet200ResponseDataActivity](docs/V1UserProfileGet200ResponseDataActivity.md)
 - [V1UserSettingsGet200Response](docs/V1UserSettingsGet200Response.md)
 - [V1UserSettingsGet200ResponseData](docs/V1UserSettingsGet200ResponseData.md)
 - [V1UserSettingsGet200ResponseDataNotifications](docs/V1UserSettingsGet200ResponseDataNotifications.md)
 - [V1UserSettingsGet200ResponseDataPlayer](docs/V1UserSettingsGet200ResponseDataPlayer.md)
 - [V1UserSettingsPatch200Response](docs/V1UserSettingsPatch200Response.md)
 - [V1UserSettingsPatchRequest](docs/V1UserSettingsPatchRequest.md)
 - [V1UserSettingsPatchRequestNotifications](docs/V1UserSettingsPatchRequestNotifications.md)
 - [V1UserSettingsPatchRequestPlayer](docs/V1UserSettingsPatchRequestPlayer.md)
 - [V1UserSettingsPatchRequestProfile](docs/V1UserSettingsPatchRequestProfile.md)
 - [V1UserWatchlistAnimeIdPatchRequest](docs/V1UserWatchlistAnimeIdPatchRequest.md)
 - [V1UserWatchlistGet200Response](docs/V1UserWatchlistGet200Response.md)
 - [V1UserWatchlistGet200ResponseDataInner](docs/V1UserWatchlistGet200ResponseDataInner.md)
 - [V1UserWatchlistPostRequest](docs/V1UserWatchlistPostRequest.md)


<a id="documentation-for-authorization"></a>
## Documentation For Authorization


Authentication schemes defined for the API:
<a id="Bearer"></a>
### Bearer

- **Type**: Bearer authentication (JWT / API-Key)


## Author

dev@gox.my.id

