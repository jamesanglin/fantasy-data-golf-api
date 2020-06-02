# fantasy_data_golf_api.DefaultApi

All URIs are relative to *http://api.sportsdata.io/golf/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**dfs_slates**](DefaultApi.md#dfs_slates) | **GET** /{format}/DfsSlatesByTournament/{tournamentid} | DFS Slates
[**injuries**](DefaultApi.md#injuries) | **GET** /{format}/Injuries | Injuries
[**injuries_historical**](DefaultApi.md#injuries_historical) | **GET** /{format}/InjuriesByHistorical | Injuries (Historical)
[**leaderboard**](DefaultApi.md#leaderboard) | **GET** /{format}/Leaderboard/{tournamentid} | Leaderboard
[**news**](DefaultApi.md#news) | **GET** /{format}/News | News
[**news_by_date**](DefaultApi.md#news_by_date) | **GET** /{format}/NewsByDate/{date} | News by Date
[**news_by_player**](DefaultApi.md#news_by_player) | **GET** /{format}/NewsByPlayerID/{playerid} | News by Player
[**player**](DefaultApi.md#player) | **GET** /{format}/Player/{playerid} | Player
[**player_season_stats_w_world_golf_rankings**](DefaultApi.md#player_season_stats_w_world_golf_rankings) | **GET** /{format}/PlayerSeasonStats/{season} | Player Season Stats (w/ World Golf Rankings)
[**player_tournament_projected_stats_w_draftkings_salaries**](DefaultApi.md#player_tournament_projected_stats_w_draftkings_salaries) | **GET** /{format}/PlayerTournamentProjectionStats/{tournamentid} | Player Tournament Projected Stats (w/ DraftKings Salaries)
[**player_tournament_stats_by_player**](DefaultApi.md#player_tournament_stats_by_player) | **GET** /{format}/PlayerTournamentStatsByPlayer/{tournamentid}/{playerid} | Player Tournament Stats By Player
[**players**](DefaultApi.md#players) | **GET** /{format}/Players | Players
[**schedule**](DefaultApi.md#schedule) | **GET** /{format}/Tournaments | Schedule
[**schedule_by_season**](DefaultApi.md#schedule_by_season) | **GET** /{format}/Tournaments/{season} | Schedule by Season


# **dfs_slates**
> list[DfsSlate] dfs_slates(format, tournamentid)

DFS Slates

### Example
```python
from __future__ import print_function
import time
import fantasy_data_golf_api
from fantasy_data_golf_api.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKeyHeader
configuration = fantasy_data_golf_api.Configuration()
configuration.api_key['Ocp-Apim-Subscription-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Ocp-Apim-Subscription-Key'] = 'Bearer'
# Configure API key authorization: apiKeyQuery
configuration = fantasy_data_golf_api.Configuration()
configuration.api_key['subscription-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['subscription-key'] = 'Bearer'

# create an instance of the API class
api_instance = fantasy_data_golf_api.DefaultApi(fantasy_data_golf_api.ApiClient(configuration))
format = 'format_example' # str | Desired response format. Valid entries are <code>XML</code> or <code>JSON</code>.
tournamentid = 'tournamentid_example' # str | The TournamentID of a tournament.  TournamentIDs can be found in the Tournaments API.  Valid entries are <code>58</code>, <code>61</code>, etc.

try:
    # DFS Slates
    api_response = api_instance.dfs_slates(format, tournamentid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->dfs_slates: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **format** | **str**| Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;. | 
 **tournamentid** | **str**| The TournamentID of a tournament.  TournamentIDs can be found in the Tournaments API.  Valid entries are &lt;code&gt;58&lt;/code&gt;, &lt;code&gt;61&lt;/code&gt;, etc. | 

### Return type

[**list[DfsSlate]**](DfsSlate.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader), [apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **injuries**
> list[Injury] injuries(format)

Injuries

### Example
```python
from __future__ import print_function
import time
import fantasy_data_golf_api
from fantasy_data_golf_api.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKeyHeader
configuration = fantasy_data_golf_api.Configuration()
configuration.api_key['Ocp-Apim-Subscription-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Ocp-Apim-Subscription-Key'] = 'Bearer'
# Configure API key authorization: apiKeyQuery
configuration = fantasy_data_golf_api.Configuration()
configuration.api_key['subscription-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['subscription-key'] = 'Bearer'

# create an instance of the API class
api_instance = fantasy_data_golf_api.DefaultApi(fantasy_data_golf_api.ApiClient(configuration))
format = 'format_example' # str | Desired response format. Valid entries are <code>XML</code> or <code>JSON</code>.

try:
    # Injuries
    api_response = api_instance.injuries(format)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->injuries: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **format** | **str**| Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;. | 

### Return type

[**list[Injury]**](Injury.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader), [apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **injuries_historical**
> list[Injury] injuries_historical(format)

Injuries (Historical)

### Example
```python
from __future__ import print_function
import time
import fantasy_data_golf_api
from fantasy_data_golf_api.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKeyHeader
configuration = fantasy_data_golf_api.Configuration()
configuration.api_key['Ocp-Apim-Subscription-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Ocp-Apim-Subscription-Key'] = 'Bearer'
# Configure API key authorization: apiKeyQuery
configuration = fantasy_data_golf_api.Configuration()
configuration.api_key['subscription-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['subscription-key'] = 'Bearer'

# create an instance of the API class
api_instance = fantasy_data_golf_api.DefaultApi(fantasy_data_golf_api.ApiClient(configuration))
format = 'format_example' # str | Desired response format. Valid entries are <code>XML</code> or <code>JSON</code>.

try:
    # Injuries (Historical)
    api_response = api_instance.injuries_historical(format)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->injuries_historical: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **format** | **str**| Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;. | 

### Return type

[**list[Injury]**](Injury.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader), [apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **leaderboard**
> Leaderboard leaderboard(format, tournamentid)

Leaderboard

### Example
```python
from __future__ import print_function
import time
import fantasy_data_golf_api
from fantasy_data_golf_api.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKeyHeader
configuration = fantasy_data_golf_api.Configuration()
configuration.api_key['Ocp-Apim-Subscription-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Ocp-Apim-Subscription-Key'] = 'Bearer'
# Configure API key authorization: apiKeyQuery
configuration = fantasy_data_golf_api.Configuration()
configuration.api_key['subscription-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['subscription-key'] = 'Bearer'

# create an instance of the API class
api_instance = fantasy_data_golf_api.DefaultApi(fantasy_data_golf_api.ApiClient(configuration))
format = 'format_example' # str | Desired response format. Valid entries are <code>XML</code> or <code>JSON</code>.
tournamentid = 'tournamentid_example' # str | The TournamentID of a tournament.  TournamentIDs can be found in the Tournaments API.  Valid entries are <code>58</code>, <code>61</code>, etc.

try:
    # Leaderboard
    api_response = api_instance.leaderboard(format, tournamentid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->leaderboard: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **format** | **str**| Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;. | 
 **tournamentid** | **str**| The TournamentID of a tournament.  TournamentIDs can be found in the Tournaments API.  Valid entries are &lt;code&gt;58&lt;/code&gt;, &lt;code&gt;61&lt;/code&gt;, etc. | 

### Return type

[**Leaderboard**](Leaderboard.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader), [apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **news**
> list[News] news(format)

News

### Example
```python
from __future__ import print_function
import time
import fantasy_data_golf_api
from fantasy_data_golf_api.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKeyHeader
configuration = fantasy_data_golf_api.Configuration()
configuration.api_key['Ocp-Apim-Subscription-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Ocp-Apim-Subscription-Key'] = 'Bearer'
# Configure API key authorization: apiKeyQuery
configuration = fantasy_data_golf_api.Configuration()
configuration.api_key['subscription-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['subscription-key'] = 'Bearer'

# create an instance of the API class
api_instance = fantasy_data_golf_api.DefaultApi(fantasy_data_golf_api.ApiClient(configuration))
format = 'format_example' # str | Desired response format. Valid entries are <code>XML</code> or <code>JSON</code>.

try:
    # News
    api_response = api_instance.news(format)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->news: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **format** | **str**| Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;. | 

### Return type

[**list[News]**](News.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader), [apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **news_by_date**
> list[News] news_by_date(format, _date)

News by Date

### Example
```python
from __future__ import print_function
import time
import fantasy_data_golf_api
from fantasy_data_golf_api.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKeyHeader
configuration = fantasy_data_golf_api.Configuration()
configuration.api_key['Ocp-Apim-Subscription-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Ocp-Apim-Subscription-Key'] = 'Bearer'
# Configure API key authorization: apiKeyQuery
configuration = fantasy_data_golf_api.Configuration()
configuration.api_key['subscription-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['subscription-key'] = 'Bearer'

# create an instance of the API class
api_instance = fantasy_data_golf_api.DefaultApi(fantasy_data_golf_api.ApiClient(configuration))
format = 'format_example' # str | Desired response format. Valid entries are <code>XML</code> or <code>JSON</code>.
_date = '_date_example' # str | The date of the game(s). <br>Examples: <code>2015-JUL-31</code>, <code>2015-SEP-01</code>.

try:
    # News by Date
    api_response = api_instance.news_by_date(format, _date)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->news_by_date: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **format** | **str**| Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;. | 
 **_date** | **str**| The date of the game(s). &lt;br&gt;Examples: &lt;code&gt;2015-JUL-31&lt;/code&gt;, &lt;code&gt;2015-SEP-01&lt;/code&gt;. | 

### Return type

[**list[News]**](News.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader), [apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **news_by_player**
> list[News] news_by_player(format, playerid)

News by Player

### Example
```python
from __future__ import print_function
import time
import fantasy_data_golf_api
from fantasy_data_golf_api.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKeyHeader
configuration = fantasy_data_golf_api.Configuration()
configuration.api_key['Ocp-Apim-Subscription-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Ocp-Apim-Subscription-Key'] = 'Bearer'
# Configure API key authorization: apiKeyQuery
configuration = fantasy_data_golf_api.Configuration()
configuration.api_key['subscription-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['subscription-key'] = 'Bearer'

# create an instance of the API class
api_instance = fantasy_data_golf_api.DefaultApi(fantasy_data_golf_api.ApiClient(configuration))
format = 'format_example' # str | Desired response format. Valid entries are <code>XML</code> or <code>JSON</code>.
playerid = 'playerid_example' # str | Unique FantasyData Player ID. Example:<code>40000019</code>.

try:
    # News by Player
    api_response = api_instance.news_by_player(format, playerid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->news_by_player: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **format** | **str**| Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;. | 
 **playerid** | **str**| Unique FantasyData Player ID. Example:&lt;code&gt;40000019&lt;/code&gt;. | 

### Return type

[**list[News]**](News.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader), [apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **player**
> Player player(format, playerid)

Player

### Example
```python
from __future__ import print_function
import time
import fantasy_data_golf_api
from fantasy_data_golf_api.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKeyHeader
configuration = fantasy_data_golf_api.Configuration()
configuration.api_key['Ocp-Apim-Subscription-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Ocp-Apim-Subscription-Key'] = 'Bearer'
# Configure API key authorization: apiKeyQuery
configuration = fantasy_data_golf_api.Configuration()
configuration.api_key['subscription-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['subscription-key'] = 'Bearer'

# create an instance of the API class
api_instance = fantasy_data_golf_api.DefaultApi(fantasy_data_golf_api.ApiClient(configuration))
format = 'format_example' # str | Desired response format. Valid entries are <code>XML</code> or <code>JSON</code>.
playerid = 'playerid_example' # str | Unique FantasyData Player ID. Example:<code>40000019</code>.

try:
    # Player
    api_response = api_instance.player(format, playerid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->player: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **format** | **str**| Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;. | 
 **playerid** | **str**| Unique FantasyData Player ID. Example:&lt;code&gt;40000019&lt;/code&gt;. | 

### Return type

[**Player**](Player.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader), [apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **player_season_stats_w_world_golf_rankings**
> list[PlayerSeason] player_season_stats_w_world_golf_rankings(format, season)

Player Season Stats (w/ World Golf Rankings)

### Example
```python
from __future__ import print_function
import time
import fantasy_data_golf_api
from fantasy_data_golf_api.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKeyHeader
configuration = fantasy_data_golf_api.Configuration()
configuration.api_key['Ocp-Apim-Subscription-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Ocp-Apim-Subscription-Key'] = 'Bearer'
# Configure API key authorization: apiKeyQuery
configuration = fantasy_data_golf_api.Configuration()
configuration.api_key['subscription-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['subscription-key'] = 'Bearer'

# create an instance of the API class
api_instance = fantasy_data_golf_api.DefaultApi(fantasy_data_golf_api.ApiClient(configuration))
format = 'format_example' # str | Desired response format. Valid entries are <code>XML</code> or <code>JSON</code>.
season = 'season_example' # str | Year of the season. <br>Examples: <code>2016</code>, <code>2017</code>.

try:
    # Player Season Stats (w/ World Golf Rankings)
    api_response = api_instance.player_season_stats_w_world_golf_rankings(format, season)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->player_season_stats_w_world_golf_rankings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **format** | **str**| Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;. | 
 **season** | **str**| Year of the season. &lt;br&gt;Examples: &lt;code&gt;2016&lt;/code&gt;, &lt;code&gt;2017&lt;/code&gt;. | 

### Return type

[**list[PlayerSeason]**](PlayerSeason.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader), [apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **player_tournament_projected_stats_w_draftkings_salaries**
> list[PlayerTournamentProjection] player_tournament_projected_stats_w_draftkings_salaries(format, tournamentid)

Player Tournament Projected Stats (w/ DraftKings Salaries)

### Example
```python
from __future__ import print_function
import time
import fantasy_data_golf_api
from fantasy_data_golf_api.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKeyHeader
configuration = fantasy_data_golf_api.Configuration()
configuration.api_key['Ocp-Apim-Subscription-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Ocp-Apim-Subscription-Key'] = 'Bearer'
# Configure API key authorization: apiKeyQuery
configuration = fantasy_data_golf_api.Configuration()
configuration.api_key['subscription-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['subscription-key'] = 'Bearer'

# create an instance of the API class
api_instance = fantasy_data_golf_api.DefaultApi(fantasy_data_golf_api.ApiClient(configuration))
format = 'format_example' # str | Desired response format. Valid entries are <code>XML</code> or <code>JSON</code>.
tournamentid = 'tournamentid_example' # str | The TournamentID of a tournament.  TournamentIDs can be found in the Tournaments API.  Valid entries are <code>78</code>, <code>79</code>, <code>80</code>, etc.

try:
    # Player Tournament Projected Stats (w/ DraftKings Salaries)
    api_response = api_instance.player_tournament_projected_stats_w_draftkings_salaries(format, tournamentid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->player_tournament_projected_stats_w_draftkings_salaries: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **format** | **str**| Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;. | 
 **tournamentid** | **str**| The TournamentID of a tournament.  TournamentIDs can be found in the Tournaments API.  Valid entries are &lt;code&gt;78&lt;/code&gt;, &lt;code&gt;79&lt;/code&gt;, &lt;code&gt;80&lt;/code&gt;, etc. | 

### Return type

[**list[PlayerTournamentProjection]**](PlayerTournamentProjection.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader), [apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **player_tournament_stats_by_player**
> PlayerTournament player_tournament_stats_by_player(format, tournamentid, playerid)

Player Tournament Stats By Player

### Example
```python
from __future__ import print_function
import time
import fantasy_data_golf_api
from fantasy_data_golf_api.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKeyHeader
configuration = fantasy_data_golf_api.Configuration()
configuration.api_key['Ocp-Apim-Subscription-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Ocp-Apim-Subscription-Key'] = 'Bearer'
# Configure API key authorization: apiKeyQuery
configuration = fantasy_data_golf_api.Configuration()
configuration.api_key['subscription-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['subscription-key'] = 'Bearer'

# create an instance of the API class
api_instance = fantasy_data_golf_api.DefaultApi(fantasy_data_golf_api.ApiClient(configuration))
format = 'format_example' # str | Desired response format. Valid entries are <code>XML</code> or <code>JSON</code>.
tournamentid = 'tournamentid_example' # str | The TournamentID of a tournament.  TournamentIDs can be found in the Tournaments API.  Valid entries are <code>58</code>, <code>61</code>, etc.
playerid = 'playerid_example' # str | Unique FantasyData Player ID. Example:<code>40000019</code>.

try:
    # Player Tournament Stats By Player
    api_response = api_instance.player_tournament_stats_by_player(format, tournamentid, playerid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->player_tournament_stats_by_player: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **format** | **str**| Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;. | 
 **tournamentid** | **str**| The TournamentID of a tournament.  TournamentIDs can be found in the Tournaments API.  Valid entries are &lt;code&gt;58&lt;/code&gt;, &lt;code&gt;61&lt;/code&gt;, etc. | 
 **playerid** | **str**| Unique FantasyData Player ID. Example:&lt;code&gt;40000019&lt;/code&gt;. | 

### Return type

[**PlayerTournament**](PlayerTournament.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader), [apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **players**
> list[Player] players(format)

Players

### Example
```python
from __future__ import print_function
import time
import fantasy_data_golf_api
from fantasy_data_golf_api.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKeyHeader
configuration = fantasy_data_golf_api.Configuration()
configuration.api_key['Ocp-Apim-Subscription-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Ocp-Apim-Subscription-Key'] = 'Bearer'
# Configure API key authorization: apiKeyQuery
configuration = fantasy_data_golf_api.Configuration()
configuration.api_key['subscription-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['subscription-key'] = 'Bearer'

# create an instance of the API class
api_instance = fantasy_data_golf_api.DefaultApi(fantasy_data_golf_api.ApiClient(configuration))
format = 'format_example' # str | Desired response format. Valid entries are <code>XML</code> or <code>JSON</code>.

try:
    # Players
    api_response = api_instance.players(format)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->players: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **format** | **str**| Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;. | 

### Return type

[**list[Player]**](Player.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader), [apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **schedule**
> list[Tournament] schedule(format)

Schedule

### Example
```python
from __future__ import print_function
import time
import fantasy_data_golf_api
from fantasy_data_golf_api.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKeyHeader
configuration = fantasy_data_golf_api.Configuration()
configuration.api_key['Ocp-Apim-Subscription-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Ocp-Apim-Subscription-Key'] = 'Bearer'
# Configure API key authorization: apiKeyQuery
configuration = fantasy_data_golf_api.Configuration()
configuration.api_key['subscription-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['subscription-key'] = 'Bearer'

# create an instance of the API class
api_instance = fantasy_data_golf_api.DefaultApi(fantasy_data_golf_api.ApiClient(configuration))
format = 'format_example' # str | Desired response format. Valid entries are <code>XML</code> or <code>JSON</code>.

try:
    # Schedule
    api_response = api_instance.schedule(format)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->schedule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **format** | **str**| Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;. | 

### Return type

[**list[Tournament]**](Tournament.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader), [apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **schedule_by_season**
> list[Tournament] schedule_by_season(format, season)

Schedule by Season

### Example
```python
from __future__ import print_function
import time
import fantasy_data_golf_api
from fantasy_data_golf_api.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKeyHeader
configuration = fantasy_data_golf_api.Configuration()
configuration.api_key['Ocp-Apim-Subscription-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Ocp-Apim-Subscription-Key'] = 'Bearer'
# Configure API key authorization: apiKeyQuery
configuration = fantasy_data_golf_api.Configuration()
configuration.api_key['subscription-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['subscription-key'] = 'Bearer'

# create an instance of the API class
api_instance = fantasy_data_golf_api.DefaultApi(fantasy_data_golf_api.ApiClient(configuration))
format = 'format_example' # str | Desired response format. Valid entries are <code>XML</code> or <code>JSON</code>.
season = 'season_example' # str | Year of the season. <br>Examples: <code>2016</code>, <code>2017</code>.

try:
    # Schedule by Season
    api_response = api_instance.schedule_by_season(format, season)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->schedule_by_season: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **format** | **str**| Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;. | 
 **season** | **str**| Year of the season. &lt;br&gt;Examples: &lt;code&gt;2016&lt;/code&gt;, &lt;code&gt;2017&lt;/code&gt;. | 

### Return type

[**list[Tournament]**](Tournament.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader), [apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

