link1 = "https://r.jina.ai/"
link2 = website_url
combined_link = link1 + link2
driver.get(combined_link)
time.sleep(2)
context = ""
pre_content = driver.find_elements(By.TAG_NAME, "pre")
for i in pre_content:
  context+= str(i.text)
driver.quit()
