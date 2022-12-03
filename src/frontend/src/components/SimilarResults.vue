<template>
    <div class="card-img-top similar-book">
        <div class="card-body">
            <router-link :to="{name: 'Book', params: { id: id } }" class="btn btn-primary">
                <img v-bind:src="cover_img" class="card-img-top" />
                <p class="card-text" style="margin-top: 15px;">
                    This book has also been called {{ selected_buzzword }} and found {{ selected_mood }}.
                </p>
            </router-link>
        </div>
    </div>
</template>

<script lang="js" >
import { defineComponent } from 'vue';

export default defineComponent({
    name: 'SearchResults',

    props: {
        cover_img: {
            type: String,
            required: true
        },

        id: {
            type: Number,
            required: true
        },
        
        mood: {
            type: String,
            required: true
        },

        buzzwords: {
            type: String,
            required: true
        },
    },

    data() {
        return {
            selected_mood: '',
            selected_buzzword: ''
        }
    },

    created() {
        this.selected_buzzword = this.buzzwords[Math.random(0, this.buzzwords.length)];
        this.selected_mood = this.mood.split(',')[Math.random(0, this.mood.length)];
    }
});
</script>

