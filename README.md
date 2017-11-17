# Web Scraping Example (DynamicIP + WebDriver + Python)

This repository produces a single docker image that combines Chrome with DynamicIP -- the resulting application can scrape websites while continuously changing the IP address the requests are coming from.

The application's steps are as follows:

1.  Launch Chrome (headless, inside docker).
2.  Navigate to `https://examples.dynamicip.com/single-page-apps/basic`.
3.  Render the DOM.
4.  Print the DOM to stdout.

## Prerequisites

You must have the following installed:

-   `docker`
-   `python`

## Usage

Run this once:

    echo YOUR_API_KEY > .dynamicip_api_key
    python setup.py

Run the scraper:

    python run.py

Please [sign up to DynamicIP](https://www.dynamicip.com) if you haven't already. There is a free usage tier.

## Browsers (Chrome, Firefox, etc.)

We currently only support `chrome` in our example application.

This is because the DynamicIP proxy server requires a username/password from its users. Unfortunately, both `chrome` and `firefox` do not allow proxy credentials to be passed in programmatically: they must be provided via the GUI.

There are two workarounds to this: 1) install an unprotected local proxy server (e.g. Squid) that forwards requests onto DynamicIP, effectively shielding the browser from having to deal with proxy credentials, or 2) install a browser extension that automatically enters the proxy credentials when requested.

To keep the example as a single docker image, we have opted to use approach (2). This benefits the user with a slight performance advantage and one less component to maintain, at the cost of being tied to `chrome`.

If you specifically require `firefox` instead of `chrome`, then please refer to our [knowledge base][help] as we may have devised a solution since this README was last updated. 

### Browser Docker Images

We use the [official Selenium docker images][selenium-docker] which are based on `ubuntu:16.04`:

    selenium/standalone-chrome:3.7.1-argon

[help]: https://help.dynamicip.com/  "DynamicIP - Knowledge Base"
[selenium-docker]: https://github.com/SeleniumHQ/docker-selenium  "Docker images for Selenium Grid Server"