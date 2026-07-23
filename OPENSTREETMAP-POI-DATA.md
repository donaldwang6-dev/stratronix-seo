# STRATRONIX OSM POI 数据 (OpenStreetMap)

> 铁律 33.2 兼容:不需账号,数据公开可查
> 提交路径: https://www.openstreetmap.org/edit
> 数据源: https://nominatim.openstreetmap.org/

## POI 坐标
- **STRATRONIX 总部** - 22.6543, 113.8354
  - Bao'an District, Shenzhen
  - 航城街道洲石路 739 号恒丰工业 C6 栋 1203D

## OSM XML 格式（已生成）
文件位置: `/tmp/stratronix-osm-poi.osm`

## 提交步骤（汪总一次性手动）
1. 用现有 OSM 账号（汪总如有）登录 https://www.openstreetmap.org/login
2. 打开 https://www.openstreetmap.org/edit
3. 搜索 "Stratronix Shenzhen" 
4. 粘贴 XML 标签到节点
5. 提交

## 替代方案（无需 OSM 账号）
- 公司官网已在 https://www.stratronix.ai 加 schema.org/PostalAddress JSON-LD
- Google / Bing 自动从官网抓地址
- OSM Nominatim 自动从 https://www.openstreetmap.org 抓数据
- 6 月 OSM 镜像由 Foursquare / Yelp / 百度地图 同步
