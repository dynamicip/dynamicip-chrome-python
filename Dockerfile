FROM dynamicip-chrome-python-base

# Performs the following steps:
# 1. Add source code.
# 2. Get python dependencies.
# 3. Set API key.
# 4. Update 'entry point' script.

ADD src                /opt/dynamicip/scraping-example
ADD requirements.txt   /opt/dynamicip/scraping-example
ADD .dynamicip_api_key /opt/dynamicip/scraping-example
RUN cd /opt/dynamicip/scraping-example && \
    /bin/bash -c "source .virtualenv/bin/activate && pip install -r requirements.txt" && \
    sudo sed -i -e "s/___APIKEY___/$(cat .dynamicip_api_key)/g" chrome_extension/authenticator.js && \
    sudo cp entrypoint.sh /opt/bin/entry_point.sh
