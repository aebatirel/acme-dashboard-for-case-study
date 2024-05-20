<template>
  <v-container>
    <v-row>
      <v-col v-for="restaurant in restaurants" :key="restaurant.id" cols="12" md="4">
        <v-card>
          <v-card-title>{{ restaurant.name }}</v-card-title>
          <v-card-subtitle>{{ restaurant.cuisine }}</v-card-subtitle>
          <v-card-text>{{ restaurant.borough }}</v-card-text>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      restaurants: []
    };
  },
  mounted() {
    axios.get('http://127.0.0.1:8000/api/restaurants')
      .then(response => {
        this.restaurants = response.data.map(restaurant => ({
          ...restaurant,
          id: restaurant._id.$oid  // ID'yi çek ve map et
        }));
      })
      .catch(error => {
        console.error('There was an error!', error);
      });
  }
};
</script>
