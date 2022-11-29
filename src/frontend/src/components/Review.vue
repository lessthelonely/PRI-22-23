<template>
    <div class="card" style="margin-bottom: 15px;">
        <div class="card-body">
            <p class="card-text" style="color: rgb(0,0,0); font-family: Cabin, sans-serif; font-size: 18px; text-align: justify;">
                {{ text }}
            </p>
        </div>
    </div>
</template>

<script lang="js">
import { defineComponent } from 'vue'

export default defineComponent({
    name: 'Review',
    props: {
        text: {
            type: Object,
            required: true
        }
    },
})
</script>