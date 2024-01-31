
**ปัญหา**

เนื่องจากการที่เลือก Heritage Baseline ของดาวเทียม Carbonite-2 ทำให้เกิดปัญหาตามมาหลายอย่าง ซึ่งเมื่อตรวจสอบและวิเคราะห์แล้ว พบว่าปัญหาใหญ่ในนั้น คือปัญหาที่อยู่ในระบบ Imaging Payload โดยที่ค่า Ground Sample Distance (GSD) และค่า Coverage Area นั้นไม่สามารถทำงานได้ตามความต้องการของ Requirement ซึ่งในความต้องการถูกระบุไว้ว่า
  1. The coverage area shall be greater than 6.5 km x 6.5 km
  2. The native Ground Sample Distance (GSD) of individual pixels of the imager shall
  be better than 1 m



**แนวทางการพัฒนาและแก้ไข**

![ภาพ](https://github.com/sasitsrirat/Imaging-Payload-Developer-Gistda/assets/55717534/c8066020-7433-4c66-a6f0-bcc23770f126)


แนวทางการแก้ไขคือเราสามารถขยับเลนส์ Secondary Mirror ออกห่างจาก Primary Mirror ได้ เพื่อให้เกิดระยะ Focal Length ที่สามารถทำงานได้ในระดับความสูงต่าง ๆ รวมทั้งสามารถแก้ไขและเปลี่ยนแปลง Pixel Sensor (อยู่ตำแหน่งเดียวกันกับ Eyepiece) เพื่อให้สามารถทำงานคลอบคลุมระยะ Coverage Area ที่เป็นความต้องการของ requirement โดยการคำนวณ สามารถหาคำตอบได้จากสมการ 𝐺𝑆𝐷 = 𝐴𝑙𝑡𝑖𝑡𝑢𝑑𝑒×𝑃𝑖𝑥𝑒𝑙 𝑆𝑖𝑧𝑒/𝐹𝑜𝑐𝑎𝑙 𝐿𝑒𝑛𝑔𝑡ℎ และสมการ 𝐶.𝐴 = 𝐺𝑆𝐷 × 𝑁 โดยให้ทั้งหมดอยู่ในหน่วย เมตร (m) เพื่อให้ง่ายต่อการคำนวณ โดยที่ GSD คือGround Sample Distance ส่วน C.A คือ Coverage Area และ N คือ Number of Pixel หรือ Pixel Size ในแนวแกน X และแกน Y
