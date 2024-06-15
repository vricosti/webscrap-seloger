// Import the Playwright library to use it
const playwright = require("playwright");

(async () => {
  // Launch a new instance of a Chromium browser
  const browser = await playwright.chromium.launch({
    // Set headless to false so you can see how Playwright is
    // interacting with the browser
    headless: false,
  });
  // Create a new Playwright context
  const context = await browser.newContext();
  // Create a new page/tab in the context.
  const page = await context.newPage();

  // Navigate to the Bright Data home page.
  let url ='https://www.seloger.com'
  await page.goto(url);

  // Wait 10 seconds (or 10,000 milliseconds)
  await page.waitForTimeout(10000);

  // Close the browser
  await browser.close();
})();