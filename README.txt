EdgeTech+ 2026 A0 HTML v6
============================

入口: poster.html
基于 v5 版式，单独存放，不覆盖 v5。

这一版的改动：
- 方案区主视觉改为 ESP32-S31 产品页上的软件栈概念图（Matter / ESP-IDF / ESP-GMF / ESP Private Agents 等）；
- 右侧标语不再压住 Matter 图标，方案卡片下方的空带分给了应用照片和说明；
- 四颗芯片的第一行统一为同一个无线图标；
- 规格统一为无线、CPU、内存 / GPIO、特长四行；ESP32-S31 写明クラシック Bluetooth；
- 方案为 Edge AI、HMI / GMF、RainMaker（含 ESP Private Agents）、MCP / Chatbot、Matter；
- 底部应用写软件方案和硬件功能，各约三句。

浏览器预览只缩放 1682×2378 画布。打印时整张画布放大到 A0（841×1189 mm）。
未做出血和 CMYK，不是印刷认证文件。

内容校对・技术核验（2026-09-24）
================================

本轮只调整可见文案和核验说明，不修改现有版式、CSS 或图片资源。

主要修正：
- 日语：修正了「端側推論」「画面体験」「測位を足します」等直译感较强的表达，并统一为更自然的产品/技术日语。
- ESP32-S31：明确 128-bit data bus + SIMD 的表述；将 PSRAM 改为「SiP 内蔵 DDR PSRAM」，避免误读为任意外接 DDR PSRAM。S31 当前官方 Datasheet 仍标注为 Preliminary，印刷前建议再次复核版本。
- ESP32-C5：规格保留 2.4/5 GHz Wi-Fi 6、Bluetooth LE、802.15.4、240 MHz、384 KB SRAM、29 GPIO；应用例从依据较弱的「无线摄像头」调整为智能家居 / 网关 / 高密度 Wi-Fi 环境。
- ESP32-H21：保留 96 MHz、320 KB SRAM、19 GPIO、片上 DC-DC、最高 20 dBm 等信息；Thread / Zigbee 不再写过细的版本号，避免超出当前产品页的明确表述。
- ESP32-H4：保留 Bluetooth 5.4、Thread 1.4 / Zigbee 3.0、双核 96 MHz、DSP、384 KB SRAM、40 GPIO、15 路触摸、外部 PSRAM，以及 Bluetooth 6.0 认证信息。
- 应用场景：将 Matter、ESP-GMF、ESP-VISION、ESP Private Agents、ESP-BLE-AUDIO 的描述改成与官方能力边界更一致的说法，避免把 Matter 等同于底层 Mesh，或把软件框架描述成超出其职责的能力。
- 日本法人：成立日期补充为 2025 年 5 月 2 日。

官方核验来源：
- ESP32-S31 Series Datasheet: https://documentation.espressif.com/esp32-s31_datasheet_en.html
- ESP32-C5 Product Page: https://www.espressif.com/en/products/socs/esp32-c5
- ESP32-H21 Product Page: https://www.espressif.com/en/products/socs/esp32-h21
- ESP32-H4 Product Page: https://www.espressif.com/en/products/socs/esp32-h4
- ESP-GMF Documentation: https://docs.espressif.com/projects/esp-gmf/en/latest/
- ESP-VISION Documentation: https://docs.espressif.com/projects/esp-vision/en/latest/
- ESP-Matter Documentation: https://docs.espressif.com/projects/esp-matter/en/latest/
- ESP Private Agents Documentation: https://docs.agents.espressif.com/
- Espressif Documentation MCP Server: https://developer.espressif.com/blog/2026/04/doc-mcp-server/
- ESP-BLE-AUDIO (ESP32-H4): https://docs.espressif.com/projects/esp-idf/en/stable/esp32h4/api-reference/bluetooth/esp-ble-audio.html
- 楽鑫ジャパン株式会社: https://www.espressif.com/ja-jp/company/about-us/jp-company

