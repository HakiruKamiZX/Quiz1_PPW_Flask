<template>
    <ion-page>
      <ion-tabs>
        <ion-router-outlet></ion-router-outlet>
        <ion-tab-bar slot="bottom">
          <ion-tab-button tab="HomePage" href="/HomePage/HomePage">
            <ion-icon :icon="triangle" />
            <ion-label>Home Page</ion-label>
          </ion-tab-button>
            
          <ion-tab-button tab="PageSecond" href="/tabs/PageSecond">
            <ion-icon :icon="ellipse" />
            <ion-label>Page 2</ion-label>
          </ion-tab-button>
        </ion-tab-bar>
      </ion-tabs>
    </ion-page>
  </template>
  
  <script lang="ts">
  import { defineComponent } from 'vue';
  import { IonTabBar, IonTabButton, IonTabs, IonLabel, IonIcon, IonPage, IonRouterOutlet } from '@ionic/vue';
  import { ellipse, square, triangle } from 'ionicons/icons';
  
  export default defineComponent({
    name: 'TabsPage',
    components: { IonLabel, IonTabs, IonTabBar, IonTabButton, IonIcon, IonPage, IonRouterOutlet },
    setup() {
      return {
        ellipse,  
        triangle,
      }
    }
  });
  </script>

  <style>
  ion-tab-bar {
    color: #FFFFFF;
}
</style>
