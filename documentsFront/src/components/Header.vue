<script setup>
import { onMounted, ref } from 'vue';
import MenuModal from './MenuModal.vue';

const changeMenu = ref(false)

const openMenu = (e) => {
    
    return changeMenu.value === false ? changeMenu.value = true : changeMenu.value = false;


}



</script>

<template class="app-header">
    <div class="header ">
        <!-- <h1>Documents Tic</h1> -->
        <div class="img-container">
            <a href="/"><img src="../assets/Documents.png" alt="" /></a>
            <h1>Documents tic</h1>
        </div>
        <nav class="nav-container">
            <ul>
                <li><a href="/"> <img src="../assets/svg/home-svgrepo-com.svg" alt=""> Inicio</a></li>
                <li><a href="/inventario"> <img src="../assets/svg/receipt-svgrepo-com.svg" alt=""> Inventario</a></li>
                <li><a href="/historial"> <img src="../assets/svg/history-svgrepo-com.svg" alt=""> Historial</a></li>
                <li><a href="/login"> <img src="../assets/svg/log-out-outline-svgrepo-com.svg" alt=""> Salir</a></li>

            </ul>

        </nav>
        <div class="container-hamburger">
            <a href="#" @click="openMenu">
                <img src="../assets/svg/menu-svgrepo-com.svg" alt="">
            </a>
        </div>


    </div>
    <MenuModal v-show="changeMenu"></MenuModal>
</template>


<style scoped>
html {
    font-size: 10px;
}

* {
    font-family: sans-serif;
    color: aliceblue;
    font-weight: bold;
    width: 100%;
}

.app-header {
    position: relative;
    
}

.header {
    position: relative;
    display: flex;
    justify-content: space-around;
    width: 100%;
    min-height: 6rem;
    background: #0074B7;
    padding: 0;
    z-index: 50;

}

.img-container {
    display: flex;
    width: 300px;
    justify-content: flex-start;
    height: 50px;
    align-self: center;
    align-items: center;
    background: #eaf0f4;
    border-radius: 5px;

}

.img-container h1 {
    display: block;
    font-family: 'Rokkitt', serif;
    font-weight: 700;
    font-size: 1.7rem;
    line-height: 1.5rem;
    width: 200px;
    color: rgb(52, 99, 181);
    text-align: center;

}

.img-container a {
    width: 110px;
    height: 50px;
}

.nav-container {
    display: flex;
    /* background: #ECEAEA; */
    width: 30%;
    justify-content: center;
    min-height: 60px;

}


.nav-container ul {
    display: flex;
    justify-content: space-around;
    /* width: 800px; */
    height: inherit;
    margin: 0;
}

.nav-container ul li a {
    display: flex;
    flex-direction: column;
    text-decoration: none;
    color: rgb(255, 252, 252);
    width: 100%;
    height: 100%;
    align-items: center;
    padding: 15px;
    font-weight: lighter;
}

.nav-container ul li {
    display: flex;
    align-items: center;
    justify-content: center;
    list-style: none;
    align-self: center;
    font-weight: bold;
    min-height: 1rem;
    width: 20%;
}

.nav-container li img {
    width: 25px;


}

.nav-container ul li:hover {
    background: #c6d7d193;
    border-radius: 3px;
    transition: all ease 0.2s;
}

.container-hamburger {
    display: none;
}

@media (max-width:950px) {
    .nav-container {
        display: none;
    }

    .container-hamburger {
        display: block;
        width: 30px;
        align-self: center;
    }

    .img-container h1 {
        display: none;
    }

    .img-container {
        background: none;
    }
}
</style>