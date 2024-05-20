<template>
  <v-container>
    <v-data-table :headers="headers" :items="restaurants" class="elevation-1">
      <template v-slot:item.actions="{ item }">
        <v-icon small @click="editItem(item)">mdi-pencil</v-icon>
        <v-icon small @click="deleteItem(item)">mdi-delete</v-icon>
      </template>
    </v-data-table>
    <v-dialog v-model="dialog" max-width="500px">
      <v-card>
        <v-card-title>
          <span class="headline">Edit Restaurant</span>
        </v-card-title>
        <v-card-text>
          <v-form ref="form">
            <v-text-field v-model="editedItem.name" label="Name"></v-text-field>
            <v-text-field v-model="editedItem.cuisine" label="Cuisine"></v-text-field>
            <v-select
              v-model="editedItem.borough"
              :items="boroughs"
              label="Borough"
            ></v-select>
          </v-form>
        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="blue darken-1" text @click="close">Cancel</v-btn>
          <v-btn color="blue darken-1" text @click="save">Save</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </v-container>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      dialog: false,
      headers: [
        { text: 'Name', value: 'name' },
        { text: 'Cuisine', value: 'cuisine' },
        { text: 'Borough', value: 'borough' },
        { text: 'Actions', value: 'actions', sortable: false }
      ],
      restaurants: [],
      boroughs: [],  // Borough isimleri için dizi
      editedItem: {
        id: '',
        name: '',
        cuisine: '',
        borough: ''
      },
      defaultItem: {
        id: '',
        name: '',
        cuisine: '',
        borough: ''
      }
    };
  },
  mounted() {
    this.fetchRestaurants();
    this.fetchNeighborhoods();
  },
  methods: {
    fetchRestaurants() {
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
    },
    fetchNeighborhoods() {
      axios.get('http://127.0.0.1:8000/api/neighborhoods')
        .then(response => {
          this.boroughs = response.data.map(neighborhood => neighborhood.name);
        })
        .catch(error => {
          console.error('There was an error!', error);
        });
    },
    editItem(item) {
      this.editedItem = Object.assign({}, item);
      this.dialog = true;
    },
    deleteItem(item) {
      axios.delete(`http://127.0.0.1:8000/api/restaurants/${item.id}`)
        .then(() => {
          this.fetchRestaurants();
        })
        .catch(error => {
          console.error('There was an error!', error);
        });
    },
    close() {
      this.dialog = false;
      this.$refs.form.reset();
    },
    save() {
      if (this.editedItem.id) {
        // Update existing restaurant
        axios.put(`http://127.0.0.1:8000/api/restaurants/${this.editedItem.id}`, this.editedItem)
          .then(() => {
            this.fetchRestaurants();
          })
          .catch(error => {
            console.error('There was an error!', error);
          });
      } else {
        console.error('No ID found for update.');
      }
      this.close();
    }
  }
};
</script>
