<div align="center">
  <h1>
    <img
      src="https://raw.githubusercontent.com/pySiriusDev/lcu-connector/main/docs/public/icon.png"
      width="80px"
    /><br />LCU Connector
  </h1>
</div>
<p align="center">
  <a href="https://lcu-connector.vercel.app/" target="_blank"
    ><img
      alt=""
      src="https://img.shields.io/badge/Website-EA4C89?style=normal&logo=dribbble&logoColor=white"
      style="vertical-align: center"
  /></a>
  <a href="https://twitter.com/_siriusbeck" target="_blank"
    ><img
      alt=""
      src="https://img.shields.io/badge/Twitter-1DA1F2?style=normal&logo=twitter&logoColor=white"
      style="vertical-align: center"
  /></a>
  <a href="https://www.instagram.com/biellviana" target="_blank"
    ><img
      alt=""
      src="https://img.shields.io/badge/Instagram-E4405F?style=normal&logo=instagram&logoColor=white"
      style="vertical-align: center"
  /></a>
</p>

## Description
This library serves to make the connection with the League Client API in a simple way, although there are others, such as [lcu-driver](https://github.com/sousa-andre/lcu-driver) (which by the way is very good), but with lcu-driver, for example, I couldn't work and structure my code the way I wanted it to, so I decided to make my own wrapper.
##### • [Documentation](https://lcu-connector.vercel.app/guide)

## Features
- Easy and fast setup
- Multi platform
- Extensible

## Example
```python
from lcu_connector import Connector

conn = Connector(start=True)

# Getting the data of the currently connected summoner
res = conn.get('/lol-summoner/v1/current-summoner')
print(res.json())

# Getting a summoner's data by name
summoner_name = 'JohnDoe'
res = conn.get('/lol-summoner/v1/summoners?name={summoner_name}')
print(res.json())

# Performing POST request
data = {
    'foo': 'bar'
}
res = conn.post('API_URL', data=data)
if res.status_code == 200:
    do_something()

conn.stop()
```

## To-do
- [x] More detailed documentation
- [ ] API event watcher
- [ ] Built-in functions for commonly used tasks (like a get_summoner_by_name())
    
