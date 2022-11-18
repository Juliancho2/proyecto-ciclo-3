<template>
    <div>
        <div class="modal_item">
            <div>

                <form @submit="onSubmit">
                    <div class="row fields_container" >
                        <div class="form-group row my-2">
                        <label for="titulo" class="col-sm-2 col-form-label">Usuario</label>
                        <div class="col-sm-6">
                            <select required class="form-select" name="" id="" v-model.trim="form.fk_clie">

                                <option :value="user.id" v-for="user in users">{{user.correo}}</option>
                            </select>
                        </div>
                    </div>
                    <div class="form-group row my-2">
                        <label for="precio" class="col-sm-2 col-form-label">Detalle orden</label>
                        <div class="col-sm-6">
                            <select required class="form-select" name="" id="" v-model.trim="form.detalle_alquiler_venta">
                                <option value="venta">Comprar</option>
                                <option value="alquiler">Alquilar</option>

                            </select>
                        </div>
                    </div>
                    </div>
                    <div class="row">
                        <div class="modal_item_body">
                            <div  class="w-100 flex-column d-flex align-items-center">
                                <img class="" :src="product.img_url" alt="">
                                <div >{{product.titulo}}</div>
                                <div class=" fw-bold">{{currencyFormatter.format(product.precio)}}
                            </div>
                            </div>
                            
                            <div class="confirm_action">
                                <h3 class="text-center">¿Confirma la orden?</h3>
                                
                                <div class=" my-3 text-center d-flex justify-content-evenly align-items-center">
                                    <button type="submit" class="btn btn-primary">Aceptar</button>
                                    <button @click="changeModal" type="button"
                                        class="btn btn-secondary">Cancelar</button>
                                </div>
                            </div>
                        </div>
                    </div>
                </form>
            </div>
        </div>
    </div>





</template>
<script setup>
import { onMounted, toRefs, ref, reactive } from 'vue';
import swal from 'sweetalert'

const emit = defineEmits(['modalActionChildren'])
const apiUser = "https://documentticapptic.onrender.com/api/usuarios/"
const users = ref([]);

const currencyFormatter = new Intl.NumberFormat("es-CO", {
                style: "currency",
                currency: "COP",
});

const changeModal = function () {
    emit('modalActionChildren', false);

}
const prop = defineProps({
    product: Object,
    itemCount: Object,
})
const { product, itemCount } = toRefs(prop);

const form = reactive({
    fk_clie: " ",
    fk_doc: product.value.id,
    detalle_alquiler_venta: " "
})

const formInventory = reactive({
    fk_id_doc: itemCount.value[0].fk_id_doc,
    cantidad_disponible: itemCount.value[0].cantidad_disponible - 1,
})

const getUsers = function () {
    fetch(apiUser)
        .then(res => res.json())
        .then(res => {
            users.value = res;
        })
}

const onSubmit = function (e) {
    e.preventDefault();
    if (itemCount.value[0].cantidad_disponible <= 0) {
        swal("Este documento ya no esta disponible.");
        changeModal();
    }
    else {
        fetch(`https://documentticapptic.onrender.com/api/inventario/${itemCount.value[0].id}/`, {
            method: "PUT",
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(formInventory)
        }).then(res =>res)

        fetch(`https://documentticapptic.onrender.com/api/pedido/`, {
            method: "POST",
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(form)
        }).then(res => {
            swal("Compra realizada con exito");
            changeModal();
        }).catch(err=> swal("Ocurrio un error"))
    }
}


onMounted(() => {

    getUsers();

})

</script>

<style scoped>
.modal_item {
    position: fixed;
    max-width: 700px;
    min-width: 600PX;
    background: rgb(242, 241, 244);
    padding: 30px 10px;
    border-radius: 10px;
    
   
}
.fields_container{
    display: flex;
    justify-content: flex-end;
    width: 90%;
    margin: 0 auto;
}

.modal_item_body {
    display: flex;
    flex-direction: column;
    align-items: center;
    
}

.modal_item_body img {
    width: 100px;
}

.confirm_action {
    display: flex;
    align-self: center;
    margin-top: 10px;
    flex-direction: column;
    justify-content: space-around;
}
</style>