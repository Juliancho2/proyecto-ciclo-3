<template>
    <nav class="nav-modal">
            <ul>
                <li><a href="/"> <img src="../assets/svg/home-svgrepo-com.svg" alt=""> Inicio</a></li>
                <li><a href="/inventario"> <img src="../assets/svg/receipt-svgrepo-com.svg" alt=""> Inventario</a></li>
                <li><a href="/historial"> <img src="../assets/svg/history-svgrepo-com.svg" alt=""> Historial</a></li>
                <li><a href="/login"> <img src="../assets/svg/log-out-outline-svgrepo-com.svg" alt=""> Salir</a></li>

            </ul>
            
        </nav>
</template>
<style scoped>

.nav-modal{
    position: absolute;
    z-index: 60;
    left: 0;
    min-height: 100px;
    background: #F2F6F4;
    display: flex;
    flex-direction: column;
    width: 40%;
    justify-content: center;
    min-height: 400px;
    transition: all 0.8s ease-in-out;
    
}


.nav-modal ul {
    display: flex;
    justify-content: space-around;
    flex-direction: column;
    height: inherit;
    margin: 0;
}

.nav-modal ul li a {
    display: flex;
    flex-direction: column;
    text-decoration: none;
    color: rgb(36, 31, 31);
    font-weight: 700;
    width: 100%;
    height: 100%;
    align-items: center;
    padding: 15px;
    font-weight: lighter;
}

.nav-modal ul li {
    display: flex;
    align-items: center;
    justify-content: center;
    list-style: none;
    align-self: center;
    font-weight: bold;
    min-height: 1rem;
    width: 40%;
}
.nav-modal ul li:hover{
    background: rgba(43, 127, 176, 0.66);
    transition: all 0.8s ease-in-out;
}
.nav-modal li img{
    width:25px;
    
    
}
</style>