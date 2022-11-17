<template>
  <ion-page>
    <ion-header :translucent="true">
      <ion-grid>
        <ion-row>
          <ion-col color="light" size="0.8">
            <ion-img src="assets/icon/prev.png"> </ion-img>
          </ion-col>
          <ion-col>
            <ion-title style="text-align:center">Registrasi</ion-title>
          </ion-col>
        </ion-row>
      </ion-grid>
    </ion-header>

    <ion-content :fullscreen="true">
      <ion-header colloapse="condense">
      </ion-header>


      <ion-list>
        <!-- Card1 -->
        <ion-grid>
          <ion-item>
            <ion-label margin="30px"><strong>Nama Kolam</strong></ion-label>
          </ion-item>
          <ion-card>
            <ion-card-content>
              <ion-grid>
                <ion-row>
                  <ion-col>
                    <ion-col>
                      <ion-input placeholder="Kolam Nila" v-model="nama_kolam"></ion-input>
                    </ion-col>
                  </ion-col>
                </ion-row>
              </ion-grid>
            </ion-card-content>
          </ion-card>
        </ion-grid>
        <!-- Card1 -->

        <!-- Card1 -->
        <ion-grid>
          <ion-item>
            <ion-label margin="30px"><strong>Lokasi Kolam</strong></ion-label>
          </ion-item>
          <ion-card>
            <ion-card-content>
              <ion-grid>
                <ion-row>
                  <ion-col>
                    <ion-col>
                      <ion-input placeholder="Bekasi Utara" v-model="lokasi_kolam"></ion-input>
                    </ion-col>
                  </ion-col>
                </ion-row>
              </ion-grid>
            </ion-card-content>
          </ion-card>
        </ion-grid>
        <!-- Card1 -->

        <!-- Card1 -->
        <ion-grid>
          <ion-item>
            <ion-label margin="30px"><strong>Material Kolam</strong></ion-label>
          </ion-item>
          <ion-card>
            <ion-card-content>
              <ion-grid>
                <ion-row>
                  <ion-col>
                    <ion-col>
                      <ion-select interface="action-sheet" v-model="material_kolam">
                        <ion-select-option value="tanah">tanah</ion-select-option>
                        <ion-select-option value="terpal">terpal</ion-select-option>
                        <ion-select-option value="beton">beton</ion-select-option>
                      </ion-select>
                    </ion-col>
                  </ion-col>
                </ion-row>
              </ion-grid>
            </ion-card-content>
          </ion-card>
        </ion-grid>
        <!-- Card1 -->

        <!-- Card1 -->
        <ion-grid>
          <ion-item color="light">
            <ion-label margin="30px"><strong>Bentuk Kolam</strong></ion-label>
          </ion-item>
          <ion-card>
            <ion-card-content>
              <ion-grid>
                <ion-row>
                  <ion-col>
                    <ion-col>
                      <ion-select interface="action-sheet" v-model="bentuk_kolam">
                        <ion-select-option value="kotak">Kotak</ion-select-option>
                        <ion-select-option value="bundar">Bundar</ion-select-option>
                      </ion-select>
                    </ion-col>
                  </ion-col>
                </ion-row>
              </ion-grid>
            </ion-card-content>
          </ion-card>
        </ion-grid>
        <!-- Card1 -->

        <ion-list style="text-align:center">
          <ion-button slot="end" size="large" color="tertiary">
            <div style="color: white;">
              <strong>Registrasi</strong>
            </div>
          </ion-button>
        </ion-list>

      </ion-list>
    </ion-content>
  </ion-page>
</template>


<script lang="ts">
import { IonHeader, IonPage, IonTitle, IonToolbar, IonCol, IonGrid, IonRow, IonContent, IonCard, IonCardContent, IonImg, IonList, IonItem, IonLabel, IonButton, IonIcon, IonInput, IonSelect, IonSelectOption } from '@ionic/vue';
import { defineComponent } from 'vue';
import { calendarOutline } from 'ionicons/icons';
import * as Vue from 'vue' // in Vue 3
import axios from 'axios'
import VueAxios from 'vue-axios'




export default defineComponent({
  components: {
    IonHeader, IonPage, IonTitle, IonGrid, IonRow, IonCol, IonContent, IonList, IonItem, IonLabel, IonCard, IonButton, IonCardContent, IonImg, IonInput, IonSelect, IonSelectOption
  },
  data() {
    return {
      nama_kolam: '',
      lokasi_kolam: '',
      material_kolam: '',
      bentuk_kolam: '',
    }
  },
  methods: {
    getFormValues() {
      console.log(this.nama_kolam)
      console.log(this.lokasi_kolam)
      console.log(this.material_kolam)
      console.log(this.bentuk_kolam)

      var pond = { 'nama': this.nama_kolam, 'lokasi': this.lokasi_kolam, 'material': this.material_kolam, 'bentuk': this.bentuk_kolam }
      console.log(pond)

      const app = Vue.createApp(...)
      app.use(VueAxios, axios)
    }
  }
});
</script>

<style scoped>
#container {
  text-align: center;

  position: absolute;
  left: 0;
  right: 0;
  top: 50%;
  transform: translateY(-50%);
}

#container strong {
  font-size: 20px;
  line-height: 26px;
}

#container p {
  font-size: 16px;
  line-height: 22px;
  color: #8c8c8c;
  margin: 0;
}

#container a {
  text-decoration: none;
}

template {
  font-family: 'Poppins';
}

ion-list {
  background-color: #121212;
}

ion-item {
  background-color: #FFFFFF;
}

ion-title {
  color: #FFFFFF;
}

ion-col {
  font-family: 'Poppins';
  color: #FFFFFF;
  font-weight: bold;
  font-size: 16px
}


ion-card {
  background: #2F2C40;
  flex-direction: row;
  border-radius: 20px;
  width: 90%;
  margin: 20px;
}

ion-button {
  width: 90%;
  align-self: center;
}
</style>