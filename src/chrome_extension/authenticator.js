var proxyHost        = 'dynamicip.com';
var proxyCredentials = {
  authCredentials: {
    username: 'apikey',
    password: '___APIKEY___'
  }
};

chrome.webRequest.onAuthRequired.addListener(
  function(challenge) {
    var isExpectedProxy = challenge.isProxy && challenge.challenger.host == proxyHost;
    return isExpectedProxy ? proxyCredentials : null;
  }, {
    urls: [ '<all_urls>' ]
  }, [
    'blocking'
  ]
);