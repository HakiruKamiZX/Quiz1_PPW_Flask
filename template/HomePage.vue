<template>
  <ion-page>
      <div id="container">
      </div>
  </ion-page>

  <ion-header>
    <ion-toolbar>
      <ion-buttons slot="start">
        <ion-back-button></ion-back-button>
      </ion-buttons>
      <ion-title>Home</ion-title>
    </ion-toolbar>
  </ion-header>
  
  <ion-grid>
  <ion-row>
    <ion-col>
      <ion-card >
        <ion-card-header>
        <ion-card-title>Kolam</ion-card-title>
        <ion-card-subtitle>10</ion-card-subtitle>
          </ion-card-header>
        <ion-card-content>
        </ion-card-content>
      </ion-card>
    </ion-col>

    <ion-col>
      <ion-card>
        <ion-card-header>
        <ion-card-title>Kolam Aktif</ion-card-title>
        <ion-card-subtitle>8</ion-card-subtitle>
        </ion-card-header>

       <ion-card-content>
       </ion-card-content>
      </ion-card>
    </ion-col>
  </ion-row>
  <ion-row>
    <ion-col>
      <ion-card>
        <ion-card-header>
        <ion-card-title>Ikan Hidup</ion-card-title>
        <ion-card-subtitle>182 Ekor</ion-card-subtitle>
          </ion-card-header>
        <ion-card-content>
        </ion-card-content>
      </ion-card>
    </ion-col>

    <ion-col>
      <ion-card>
        <ion-card-header>
        <ion-card-title>Ikan Mati</ion-card-title>
        <ion-card-subtitle>89 Ekor</ion-card-subtitle>
        </ion-card-header>

       <ion-card-content>
       </ion-card-content>
      </ion-card>
    </ion-col>
  </ion-row>

  <ion-row>
    <ion-col>
      <ion-card>
        <ion-card-header>
        <ion-card-title>Panen 2022</ion-card-title>
        <ion-card-subtitle>109 Kg</ion-card-subtitle>
          </ion-card-header>
        <ion-card-content>
        </ion-card-content>
      </ion-card>
    </ion-col>

    <ion-col>
      <ion-card>
        <ion-card-header>
        <ion-card-title>Total Pakan</ion-card-title>
        <ion-card-subtitle>223 Kg</ion-card-subtitle>
        </ion-card-header>

       <ion-card-content>
       </ion-card-content>
      </ion-card>
    </ion-col>
  </ion-row>
</ion-grid>

<ion-header>
    <ion-toolbar>
      <ion-buttons slot="start">
        <ion-back-button></ion-back-button>
      </ion-buttons>
      <ion-title>TOTAL BERAT IKAN</ion-title>
    </ion-toolbar>
  </ion-header>

<ion-grid>
  <ion-row>
    <ion-col>
      <ion-card style=" height : 100%">
        <ion-card-header>
          <img src="https://img-cdn.medkomtek.com/c4d6vF_ynGBgFgde119R1Wt7u8Q=/0x0/smart/filters:quality(75):strip_icc():format(webp)/article/CB8IhdEffuPxRdOFkd192/original/057465700_1582721737-Viral-Bintik-Putih-di-Daging-Ikan-Lele-Bolehkah-Dimakan-shutterstock_385414768.jpg" alt="">
        <ion-card-title>LELE</ion-card-title>
        <div1 ion-card-subtitle>200 Kg</div1>
        </ion-card-header>
       <ion-card-content>
       </ion-card-content>
      </ion-card>
    </ion-col>

    <ion-col>
      <ion-card style="height : 100%">
        <ion-card-header> 
          <img src="https://cdnwpseller.gramedia.net/wp-content/uploads/2022/07/05184921/Ikan-Nila-1.jpg" alt="">
        <ion-card-title>NILA MERAH</ion-card-title>
        <div1 ion-card-subtitle>200 Kg</div1>
        </ion-card-header>
       <ion-card-content>
       </ion-card-content>
      </ion-card>
    </ion-col>
  </ion-row>
</ion-grid>

<ion-header>
    <ion-toolbar>
      <ion-buttons slot="start">
        <ion-back-button></ion-back-button>
      </ion-buttons>
      <ion-title>KUALITAS AIR</ion-title>
    </ion-toolbar>
  </ion-header>

  <ion-grid>
    <ion-row>
      <ion-col>
        <ion-card>
        <ion-card-header>
        <div2 ion-card-title>pH</div2>
        <ion-card-content>
          
        </ion-card-content>
        <div4 ion-card-subtitle>Normal :<div3>6 Kolom</div3></div4>
        <ion-card-content>
          
        </ion-card-content>
        <div4 ion-card-subtitle>Abnormal :<div3>6 Kolom</div3></div4>
        </ion-card-header>
       <ion-card-content>
       </ion-card-content>
      </ion-card>
      </ion-col>

      <ion-col>
        <ion-card>
        <ion-card-header>
        <div2 ion-card-title>DO</div2>
        <ion-card-content>
          
        </ion-card-content>
        <div4 ion-card-subtitle>Normal :<div3>6 Kolom</div3></div4>
        <ion-card-content>

        </ion-card-content>
        <div4 ion-card-subtitle>Abnormal :<div3>6 Kolom</div3></div4>
        </ion-card-header>

       <ion-card-content>
       </ion-card-content>
      </ion-card>
      </ion-col>
    </ion-row>
  </ion-grid>



</template>

<script lang="ts">
import { IonHeader, IonPage, IonTitle, IonToolbar, IonCol, IonGrid, IonRow, IonCard, IonCardContent, IonCardHeader, IonCardSubtitle, IonCardTitle} from '@ionic/vue';
import { defineComponent } from 'vue';



export default defineComponent({
  name: 'HomePage',
  components: {
    IonHeader,
    IonPage,
    IonTitle,
    IonToolbar,
    IonCol,
    IonGrid,
    IonRow,
    IonCard, 
    IonCardContent, 
    IonCardHeader, 
    IonCardSubtitle, 
    IonCardTitle
  },
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

ion-col {
    background-color: #121111;
    border: solid 1px #121111;
    color: rgb(0, 0, 0);
    text-align: left;
  }

  ion-card {
    background:#FFFFFF;
    flex-direction: column;
    width: 90% ;
    margin: 10 ;

  }
  ion-card-header.ios {
    display: flex;
    flex-flow: column-reverse;
    background-color: #8c8c8c;
  }

  ion-card-title {
    color:#000000;
    font-size: 18px;
  }

  ion-card-subtitle{
    color:#000000;
    font-size: 40px;
  }

  ion-card-subtitle1{
    color:#000000;
    font-size: 40px;
  }
  
  div1{
    color:aqua;
    font-size: 40px;
  }

  div2{
    color:rgb(0, 0, 0);
    font-size: 40px;
  }

  div3{
    color:aqua;
    font-size: 20px;
  }

  div4{
    color:rgb(0, 0, 0);
    font-size: 20px;
  }

</style>
