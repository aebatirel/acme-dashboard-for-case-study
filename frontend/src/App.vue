<template>
  <v-app>
    <v-navigation-drawer app v-model="drawer" temporary>
      <v-list dense>
        <v-list-item>
          <v-list-item-content>
            <v-list-item-title>Menu</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
        <v-list-item link :to="{ name: 'Restaurants' }">
          <v-list-item-content>
            <v-list-item-title>Restaurants</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
        <v-expansion-panels>
          <v-expansion-panel>
            <v-expansion-panel-title v-slot:default="{ expanded }">
              <v-row no-gutters>
                <v-col class="d-flex justify-start" cols="12">
                  Management
                </v-col>
              </v-row>
            </v-expansion-panel-title>
            <v-expansion-panel-text>
              <v-list-item link :to="{ name: 'EditRestaurants' }">
                <v-list-item-content>
                  <v-list-item-title>Edit Restaurants</v-list-item-title>
                </v-list-item-content>
              </v-list-item>
            </v-expansion-panel-text>
          </v-expansion-panel>
        </v-expansion-panels>
      </v-list>
    </v-navigation-drawer>
    <v-app-bar app>
      <v-app-bar-nav-icon @click="drawer = !drawer"></v-app-bar-nav-icon>
      <v-toolbar-title>Acme Dashboard</v-toolbar-title>
    </v-app-bar>
    <v-main>
      <router-view></router-view>
    </v-main>
  </v-app>
</template>

<script>
export default {
  data() {
    return {
      drawer: false
    };
  }
};
</script>

<style>
@import 'vuetify/styles';
@import '@mdi/font/css/materialdesignicons.css';

.v-list-item-title {
  padding-left: 16px;
}
</style>
