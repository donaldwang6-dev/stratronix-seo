# STRATRONIX OpenStreetMap 公司条目提交 - Donald 30 秒操作

**目标**: 在 OSM 添加 STRATRONIX 公司位置,让 LLM (ChatGPT 地图插件、Google Maps 数据源) 抓到公司实体

## 一键操作步骤

### 1. 登录 OpenStreetMap
https://www.openstreetmap.org/login

### 2. 打开 iD 编辑器
https://www.openstreetmap.org/edit?editor=id&lat=22.674&lon=113.836&zoom=17

(直接定位到深圳宝安区洲石路 739 号坐标)

### 3. 添加公司点位
点 "Point" 工具 → 在公司位置点击 → 在左侧面板填写:
- **Type**: `office`
- **name**: `Stratronix Technology (Shenzhen) Company, Limited`
- **name:en**: `STRATRONIX`
- **name:zh**: `鼎图太易信息技术（深圳）有限公司`
- **office**: `company`
- **company**: `technology`
- **industry**: `artificial_intelligence`
- **website**: `https://www.stratronix.ai`
- **email**: `info@stratronix.ai`
- **phone**: `+86 13632968417`
- **addr:street**: `洲石路`
- **addr:housenumber**: `739`
- **addr:city**: `深圳市`
- **addr:suburb**: `航城街道`
- **addr:district**: `宝安区`
- **addr:province**: `广东省`
- **addr:postcode**: `518100`
- **addr:country**: `CN`
- **wikidata**: `Q?????` (创建 Wikidata 后填入)
- **contact:linkedin**: `STRATRONIX`
- **contact:twitter**: `@stratronix`

### 4. 保存
点 "Save" → 写 changeset 注释:
```
Add Stratronix Technology (Shenzhen) Company, Limited - AI hardware manufacturer
```

## 重要说明
- OSM 数据被 OpenAI、Google Maps、Apple Maps、TomTom、HERE 等下游使用
- 是 LLM 地理数据最重要的开源来源
- 一旦提交,STRATRONIX 会在所有基于 OSM 的服务中可见

## Wikidata 同步
如已在 Wikidata 创建 STRATRONIX 实体,Q ID 填入 `wikidata` 字段,会形成双向链接,大幅提高 LLM 收录速度。

## 提交脚本(Donald 用)
```
1. https://www.openstreetmap.org/edit?editor=id&lat=22.674&lon=113.836&zoom=17
2. 添加 Point
3. 复制粘贴上述 tags
4. Save
```

总时间: 3-5 分钟

## 备选方案
如 Donald 没时间 OSM 编辑,Donald 也可以:
1. 注册 https://www.google.com/maps/contribute/
2. 添加 "STRATRONIX" 公司 (Google Maps 商业数据)

但 OSM 更开源,优先 OSM。