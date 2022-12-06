<template>
    <WhiteHeader />

    <body id="page-top" data-bs-spy="scroll" data-bs-target="#mainNav" data-bs-offset="77" style="background: rgb(255,255,255);">
        <div class="container">
            <div class="col">
                <div class="row">
                    <div class="col">
                        <div class="row" style="margin-bottom: 30px;">
                            <div class="col-md-5" style="width: 30%;">
                                <div class="row" style="margin-bottom: 15px;">
                                    <div class="col">
                                        <picture>
                                            <img style="width: 100%;height: auto;max-height: 100%;" v-bind:src="picture" v-if="(picture!='')" />
                                            <img style="width: 100%;height: auto;max-height: 100%;" src="../assets/images/placeholder_author.png" v-else/>
                                        </picture>
                                    </div>
                                </div>
                                <div class="row">
                                    <div class="col text-start">
                                        <div></div>
                                    </div>
                                </div>
                            </div>
                            <div class="col">
                                <div class="row">
                                    <div class="col">
                                        <h1 class="text-start" style="color: rgb(0,0,0);margin: 0px;">{{name}}</h1>
                                        <h4 v-if="birthplace!=''" class="text-start" style="color: rgb(109,109,109);margin: 0px;margin-bottom: 15px;">{{birthplace}}</h4>
                                    </div>
                                </div>
                                <div class="row">
                                    <div class="col">
                                        <h6 v-if="genres!=''" class="text-start" style="color: rgb(194,194,194);margin: 0px;margin-bottom: 15px;">{{genres}}</h6>
                                    </div>
                                </div>
                                <div class="row" style="margin-top: 15px;" v-if="abstract!=''">
                                    <div class="col" style="height: 311px;">
                                        <h3 class="text-start" style="color: rgb(0,0,0);margin: 0px;margin-bottom: 15px;">Abstract</h3>
                                        <p style="text-align: justify; font-family: Arial;color: rgb(0,0,0);font-size: 19px;height: 80%;">{{abstract}}</p>
                                    </div>
                                </div>
                            </div>
                        </div>
                        <div class="row" style="margin-bottom: 30px;">
                            <div class="col flex-column">
                                <h1 class="text-start" style="margin: 0px;margin-bottom: 15px;">
                                    <span style="color: rgb(0, 0, 0);">Books</span>
                                </h1>
                                <div class="row" style="display: flex; flex-wrap: wrap; flex-direction: row; justify-content: center;">
                                    <SimilarResults v-bind:cover_img="book.cover_img" v-bind:buzzwords="book.buzzwords.toString()"
                                    v-bind:id="book.id" v-bind:mood="book.mood.toString()" v-bind:rating="book.rating"
                                    v-for="book in books" v-if="(books.length != 0)" />
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </body>
</template>

<script lang="js" >
import { defineComponent } from 'vue';
import WhiteHeader from '../components/WhiteHeader.vue';
import SimilarResults from '../components/SimilarResults.vue';
import axios from 'axios';

export default defineComponent({
    name: 'Author',

    components: {
        WhiteHeader,
        SimilarResults
    },

    data() {
        return {
            name: '',
            birthplace: '',
            genres: '',
            abstract: '',
            picture: '',
            books: []
        };
    },

    methods: {

    },

    created() {
        this.name = this.$route.params.name;

        axios.get("/author/" + this.$route.params.name)
        .then(response => {
            this.birthplace = response.data.birth;
            this.genres = response.data.genres;
            this.abstract = response.data.abstract;
            this.picture = response.data.image;
            this.books = response.data.books;
        })
    }
});
</script>