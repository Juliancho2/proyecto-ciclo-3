<template>
    <Header></Header>
    <div class="container">
        <div v-if="openEdit">
            <EditDocuments :open="open" :idItem="objectFilter[0]" @openChildren="openChildren">
            </EditDocuments>
        </div>
        <div v-else-if="openAdd">
            <AddDocument @closeAdd="closeAdd"></AddDocument>
        </div>


        <h2>Lista de documentos</h2>
        <hr>
        <button @click="openAddDocument" class="btn-add rounded-1">Añadir <img src="../assets/close-icon.svg" alt="">
        </button>

        <div class="list-grid-titles">
            <h4>Id</h4>
            <h4>Titulo</h4>
            <h4>Autor</h4>
            <h4>Precio</h4>
            <h4>Tipo documento</h4>
            <h4>Categoria</h4>
            <h4>Cantidad disponible</h4>

            <h4>Accion</h4>
        </div>
        <div class="list-grid-documents">
            <div class="list-grid-items" v-for="item in array" :id="item.id" v-if="!loader">
                <p>{{item.id}}</p>
                <p>{{item.titulo}}</p>
                <p>{{item.nombre_autor}}</p>
                <p>{{amountCurrecy(item.precio)}}</p>
                <p>{{item.tipo_doc}}</p>
                <p>{{item.categoria}}</p>
                <p>{{getIdInventary(item.id)[0].cantidad_disponible}}</p>
                <div class="btn-action">
                    <a class="btn-edit" @click="openEditDocument(item.id)"><img src="../assets/pngwing.com.png"
                            alt="Editar" title="Editar"></a>
                    <a class="btn-remove" @click="onDeleteDocument(item.id)"><img src="../assets/trash-icon.svg"
                            alt="Eliminar" title="Eliminar"></a>
                </div>


            </div>
            <div v-else class="loader-container">
                <span class="loader"></span>
            </div>

        </div>
    </div>
</template>







<script >
import Header from "./Header.vue";
const apiProducts = "https://documentticapptic.onrender.com/api/productos/"

import { ref } from 'vue';
import EditDocuments from "./EditDocuments.vue";
import AddDocument from "./AddDocument.vue";


export default {

    data() {
        return {
            idDocument: ref(""),
            array: ref([]),
            loader: ref(true),
            openEdit: ref(false),
            openAdd: ref(false),
            idItem: ref(""),
            objectFilter: " ",
            inventary: ref([]),

        }
    },


    methods: {
        getDocuments() {

            fetch(apiProducts)
                .then(res => {
                    return res.json()
                })
                .then(json => {

                    this.array = json
                    this.loader = false
                    this.getInventary();
                })
                .catch(err => {
                    return console.log(err)
                })
        },
        openEditDocument(id) {
            this.idItem = id;
            this.openEdit = true;
            this.objectFilter = this.array.filter((el) => {
                return el.id == id;
            })

        },
        openAddDocument() {
            this.openAdd = true;
        },
        openChildren(value) {
            this.openEdit = value;
        },
        closeAdd(value) {
            this.openAdd = value;
        },

        onDeleteDocument(id) {
            const path = `https://documentticapptic.onrender.com/api/productos/${id}/`

            fetch(path, {
                method: 'DELETE',
            }).then(res => {
                location.href = '/inventario'
            }).catch(err => swal("Ocurrio un error", "error"))
        },
        getInventary() {
            fetch("https://documentticapptic.onrender.com/api/inventario/")
                .then(res => res.json())
                .then(res => {
                    
                    this.inventary = res;
                }).catch(err => console.log(err))
        },
        getIdInventary(id) {
            return this.inventary.filter(el => {
                return el.fk_id_doc == id
            })
        },
        amountCurrecy(item) {
            const currencyFormatter = new Intl.NumberFormat("es-CO", {
                style: "currency",
                currency: "COP",
            })
           return currencyFormatter.format(item)
        }

    },
    mounted() {
        this.getDocuments();


    },


    components: {
        Header,
        EditDocuments,
        AddDocument,
    },
}



</script>



<style scoped>
.container {
    display: flex;
    flex-direction: column;
    min-width: 850px;
    margin: 50px auto;
    font-family: 'Open Sans', sans-serif;

}

.container h2 {
    font-size: 2rem;
    font-weight: 600;
}

hr {
    border: 1px solid rgb(112, 109, 107);
}

.list-grid-titles {
    display: grid;
    width: 100%;
    grid-template-columns: repeat(8, 1fr);
    background: rgb(200, 196, 192);
    min-height: 40px;
    gap: 5px;
    text-align: center;

}

.list-grid-titles h4 {
    font-size: 1.2rem;
    height: 100%;
}

.list-grid-documents {
    background: rgba(250, 248, 246, 0.998);
    text-align: center;
    border: 0.5px solid #bec7c7;
}

.list-grid-items {
    display: grid;
    grid-template-columns: repeat(8, 1fr);
    width: 100%;
    background: #fff;
}

.list-grid-items p,
.list-grid-items div {
    border-top: 1px solid hsl(180, 17%, 81%);

}

.list-grid-documents p {
    display: inline-block;
    height: 100%;
    border-left: 1px solid hsl(180, 15%, 80%);
    border-right: 1px solid #c1d2d2;
    padding: 2px 1px;
}


.list-grid-documents img,
.list-grid-documents svg {
    width: 25px;
}

.btn-remove,
.btn-edit {
    cursor: pointer;
}

.btn-add img {
    transform: rotate(45deg);
    width: 15px;
    margin: 0 3px;
}

.btn-add {
    border: none;
    background: #0074b7d3;
    color: #ffff;
    font-weight: bold;
    padding: 5px;
    margin: 10px 0;
    align-self: flex-end;
    max-width: 150px;
    cursor: pointer;
}

.container .btn-action {
    display: flex;
    justify-content: space-around;
    width: 100%;
    align-items: flex-start;
    padding: 5px 0;
}

.loader-container {
    width: 100%;
    text-align: center;
}

.loader {
    margin-top: 40px;
    width: 48px;
    height: 48px;
    border-radius: 50%;
    display: inline-block;
    position: relative;
    border: 10px solid;
    border-color: rgba(25, 23, 23, 0.15) rgba(74, 71, 71, 0.25) rgba(87, 77, 77, 0.35) rgba(107, 102, 102, 0.346);
    box-sizing: border-box;
    animation: rotation 1s linear infinite;

}

@keyframes rotation {
    0% {
        transform: rotate(0deg);
    }

    100% {
        transform: rotate(360deg);
    }
}
</style>

