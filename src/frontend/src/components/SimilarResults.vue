<template>
    <div class="card-img-top similar-book">
        <div class="card-body">
            <router-link :to="{ name: 'Book', params: { id: id } }" class="btn btn-primary">
                <img v-bind:src="cover_img" class="card-img-top" />
                <div class="row" style="text-align: center; display: flex; justify-content: center; margin-top: 10px;">
                    <h3 class="text-center d-md-flex justify-content-md-center align-items-md-center"
                        style="height: auto; color: rgb(0, 0, 0); width: auto;">
                        {{ rating }}
                    </h3>
                    <FontAwesomeIcon icon="fa-star" style="color: black; font-size: 30px; margin-left: 5px;" />
                </div>
                <p class="card-text" style="margin-top: 15px;">
                    This book is {{ selected_buzzword }} {{ selected_mood }}.
                </p>
            </router-link>
        </div>
    </div>
</template>

<script lang="js" >
import { defineComponent } from 'vue';

export default defineComponent({
    name: 'SimilarResults',

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

        rating: {
            type: Number,
            required: true
        }
    },

    data() {
        return {
            selected_mood: '',
            selected_buzzword: ''
        }
    },

    methods: {
        between(min, max) {
            return Math.floor(Math.random() * (max - min) + min);
        }
    },

    created() {
        if (this.buzzwords != null) {
            var buzzwords = this.buzzwords.split(',');
            var randomBuzzword1 = this.between(0, buzzwords.length);
            this.selected_buzzword = buzzwords[randomBuzzword1];
        }

        if (this.mood != null) {
            var moods = this.mood.split(',');
            var randomMood1 = this.between(0, moods.length);
            this.selected_mood = " and readers felt " + moods[randomMood1];
        }

    }
});
</script>

