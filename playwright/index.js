// Import the Playwright library to use it
const playwright = require("playwright");
const fs = require('fs');

(async () => {
  // Launch a new instance of a Chromium browser
  const browser = await playwright.firefox.launch({
    // Set headless to false so you can see how Playwright is
    // interacting with the browser
    headless: false,
    args: ["-fullscreen"],
  });
  // Create a new Playwright context
  const context = await browser.newContext();
  const page = await context.newPage();

  let url ='https://www.seloger.com'
  await page.goto(url);

  await page.context().storageState({ path: 'data/data.json' });

  // Wait 10 seconds (or 10,000 milliseconds)
  await page.waitForTimeout(10000);

  // Close the browser
  await context.close();
})();