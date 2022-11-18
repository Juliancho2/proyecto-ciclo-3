<template>
    <Header></Header>
    <div class="container">
        <h2>Historial</h2>
        <div class="container_circle">
            <h4>Venta</h4>
            <div class="circle_resume">
               <div class="fs-3"> {{saleResume.length}}</div>
            </div>
            <h4>Alquiler</h4>

            <div class="circle_resume">
                <div class="fs-3">{{rentalResume.length}}</div>
            </div>
        </div>
        <hr>
        <table class="table table-bordered">
            <thead>
                <tr>
                    <th scope="col">Id</th>
                    <th scope="col">Fecha</th>
                    <th scope="col">Usuario</th>
                    <th scope="col">Titulo</th>
                    <th scope="col">Direccion</th>
                    <th scope="col">Detalle</th>
                    <th scope="col">Tipo</th>
                    <th scope="col">Total</th>
                </tr>
            </thead>
            <tbody>
                <tr v-for="item in record">
                    <th scope="row">{{item.id}}</th>
                    <td>{{item.fecha_pedido}}</td>
                    <td>{{item.cliente}}</td>
                    <td>{{item.titulo}}</td>

                    <td>{{item.direccion}}</td>
                    <td>{{item.detalle_alquiler_venta}}</td>
                    <td>{{item.tipo_doc}}</td>
                    <td>{{currencyFormatter.format(item.precio)}}</td>
                </tr>
            </tbody>
        </table>

    </div>


</template>

<script setup>

import { onMounted, ref } from 'vue';
import Header from './Header.vue';
const apiRecord = "https://documentticapptic.onrender.com/api/pedido/";

const record = ref([]);
const saleResume = ref([]);
const rentalResume=ref([]);

const currencyFormatter= new Intl.NumberFormat("es-CO",{
        style:"currency",
        currency:"COP",
    });

const getRecord = function () {
    fetch(apiRecord)
        .then(res => res.json())
        .then(res => {
            record.value = res;
            saleResume.value = record.value.filter(el => {
                return el.detalle_alquiler_venta
                    == "venta"
            });

            rentalResume.value=record.value.filter(el=>{
                return el.detalle_alquiler_venta
                    == "alquiler"
            });
        })
    }

    onMounted(() => {
        getRecord();
    })








</script>

<style scoped>
.container {
    margin-top: 50px;
    max-width: 1000px;
}

hr {
    border: 1px solid rgb(112, 109, 107);
}
.table{
    margin: 50px auto;
}

.container_circle {
    display: flex;
    width: 100%;
    justify-content: center;
}

.circle_resume {
    display: flex;
    justify-content: center;
    align-items: center;
    width: 80px;
    height: 80px;
    border-radius: 50%;
    background: rgb(207, 202, 202);
    margin: 0 30px;
}
</style>

