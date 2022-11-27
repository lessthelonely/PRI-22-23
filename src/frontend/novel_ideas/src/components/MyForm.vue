<template>
    <div>
        <input type="text" placeholder="Name" v-model="name"/>
    </div>
    <div>
        <button @click="submitForm" v-bind:disabled="name.length==0">Submit</button>
    </div>
</template>

<script>
import { ref, onMounted } from 'vue'
import axios from 'axios';

export default{
    setup(){
        const name = ref('')
        const el=ref()

        const submitForm = () => {
            console.log('Form submitted. Name=', name.value);
            axios.get('http://localhost:8080/book/' + name.value).then((res) =>{
                console.log(res.data);
            });
        }

        console.log(el.value)

        onMounted(() => {
            el.value.focus()
        })

        return {
            el,
            name,
            submitForm
        }
    }
}
</script>