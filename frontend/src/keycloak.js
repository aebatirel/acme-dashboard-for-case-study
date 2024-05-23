import Keycloak from 'keycloak-js';

// Keycloak configuration
const keycloak = new Keycloak({
  url: 'http://localhost:8080',  // Keycloak server URL
  realm: 'acme-realm',           // Realm name
  clientId: 'acme-client'        // Client ID
});

export default keycloak;
