<template>
    <div class="card-img-top similar-book">
        <div class="card-body">
            <button @click="goToPage(id)" class="btn btn-primary similar-book">
                <img v-bind:src="cover_img" class="card-img-top" />
                <p class="text-center d-md-flex justify-content-md-center align-items-md-center similar-book-rating">
                    {{rating}}
                    <FontAwesomeIcon class="similar-star" icon="fa-star"/>
                </p>
                <p class="card-text" style="margin-top: 15px;">
                    This book is {{ selected_buzzword }} {{ selected_mood }}.
                </p>
            </button>
        </div>
    </div>
</template>

<script lang="js" >
import { defineComponent } from 'vue';
import router from '../router';

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
        },

        goToPage(id) {
            router.push({ name: 'Book', params: { id: id } });
            window.location.href = "/book/" + id;
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

