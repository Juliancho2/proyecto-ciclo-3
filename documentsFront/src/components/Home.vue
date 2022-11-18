<template>
    <Header></Header>

<div class="home">
    <div >
        <ModalBuy class="modal_container" v-if="modalAction" :product="product[0]" :itemCount="itemCount"
            @modalActionChildren="modalActionChildren">
        </ModalBuy>

    <div class="container  py-4">


   <div class="container_input">
    <img src="../assets/svg/search-svgrepo-com.svg" alt="">
    <input type="search" v-on:keyup="searchData" class="input-search"
                placeholder="Buscar..." />
   </div>

            <div class="row">

            



                <div   class="item_card col- col-lg- col-xl-4 my-2" v-for="item in array.value">

                    <div class="card">
                        <img :src="item.img_url" class="card-img-top" :alt="item.titulo">
                        <div class="price ">{{currencyFormatter.format(item.precio)}}</div>
                        
                        <div class="card-body">

                            <h5 class="card-title">{{item.titulo}}</h5>
                            <p class="card-text">{{item.nombre_autor}}</p>
                            <ul class="list-group list-group-flush">

                                <li class="list-group-item">{{item.tipo_doc}}</li>
                                <li class="list-group-item">{{item.categoria}}</li>
                                <li class="list-group-item"></li>
                            </ul>
                            <div>
                                <button @click="btnActiveModal(item.id)" type="button"
                                    class="btn mx-1 btn-warning">Ordenar</button>
                            </div>
                        </div>


                    </div>
                </div>

            </div>
        </div>

    </div>
    <Footer></Footer>
</div>


</template>
<script setup>
import { computed } from '@vue/reactivity';
import { onMounted, reactive, ref } from 'vue';
import Header from './Header.vue';
import ModalBuy from './ModalBuy.vue';
import Footer from './Footer.vue'

const apiProducts = "https://documentticapptic.onrender.com/api/productos/"
const apiInventario = "https://documentticapptic.onrender.com/api/inventario/"

const array = reactive([]);
const modalAction = ref(false);
const product = ref(" ");
const inventoryObj = ref(" ")
const itemCount = ref(" ");


const getDocuments = function () {
    fetch(apiProducts)
        .then(res => {
            return res.json()
        })
        .then(json => {
            array.value = json


        })
        .catch(err => {
            return console.log(err);
        })
};

const searchData = function (e) {
    if(e.key == "Escape") e.target.value=""

   
    let itemsCards=document.querySelectorAll(".item_card ");
    itemsCards.forEach(el=>{
        el.querySelector("h5").textContent.toLowerCase()
        .includes(e.target.value.toLowerCase()) ?  el.classList.remove("filter")
                : el.classList.add("filter");
    });
}

const getInventario = function () {
    fetch(apiInventario)
        .then(res => res.json())
        .then(res => {
            inventoryObj.value = res;
            
        })
}

const modalActionChildren = function (value) {
    modalAction.value = value;


}
const currencyFormatter= new Intl.NumberFormat("es-CO",{
        style:"currency",
        currency:"COP",
    })

const btnActiveModal = function (id) {
    modalAction.value = true;
    product.value = array.value.filter(el => {
        return el.id == id;
    });
    itemCount.value = inventoryObj.value.filter(el => {
        return el.fk_id_doc == id;
    })
}



onMounted(() => {
    getDocuments();
    getInventario();
    
})


</script>

<style scoped>
.container {
    position: relative;
    margin: 0 auto;
    
}
.home{
    position: relative;
    background: #f2f6f4;
 
}


.container_input{
    display: flex;
    width: 300px;
    height: 35px;
    /* background: #e0e9e4; */
    background: #fff;
    margin: 20px 0;
    padding: 5px 0;
    
}
.container_input input[type="search"] {
    width:100%;
    height: 100%;
    border: none;
    outline: none;
    padding:0  5px;
    
}

.container_input img{
    width: 30px;
    border-right: 1px solid #b8cbc1;
    padding: 0 5px;
}

.card {
    display: grid;
    grid-template-columns: 2fr 1fr 2.5fr;
    width: 100%;
    border: none;
    box-shadow: -1px 1px 6px 0px rgba(207,195,195,0.75);
-webkit-box-shadow: -1px 1px 6px 0px rgba(207,195,195,0.75);
-moz-box-shadow: -1px 1px 6px 0px rgba(207,195,195,0.75);
border-radius: 0;
}

.card img {
    max-width: 200px;
    min-width: 150px;
    min-height: 250px;
}

.card .price {
    font-weight: bold;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 1.1rem;
}
.active{
    display: none;
}
.filter{
    visibility: hidden;
    opacity: 0;
    order: 1;
}
.modal_container {
    display: flex;
    position: absolute;
    z-index: 30;
    justify-content: center;
    align-items: flex-start;
    width: 100%;
    height: 100%; 
    
    /* border: 1px solid black;
    background: rgba(62, 59, 59, 0.79); */

 }
 header{
    width: 100%;
 }
</style>