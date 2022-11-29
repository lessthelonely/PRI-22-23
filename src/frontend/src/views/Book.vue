<template>
    <WhiteHeader />

    <body id="page-top" data-bs-spy="scroll" data-bs-target="#mainNav" data-bs-offset="77" style="background: rgb(255,255,255); display: block; width: 100%;">
        <div class="container">
            <div class="col">
                <div class="row">
                    <div class="col">
                        <div class="row" style="margin-bottom: 30px;">
                            <div class="col-md-5" style="width: 30%; display: flex; flex-direction: column;">
                                <div class="row" style="margin-bottom: 30px;">
                                    <div class="col">
                                        <img v-bind:src="cover_img" style="width: 100%;font-size: 16px; box-shadow: 2px 2px 9px 2px rgb(0 0 0 / 26%);">
                                    </div>
                                </div>
                                <div class="row" style="text-align: center; display: flex; justify-content: center;">
                                    <h1 class="text-center d-md-flex justify-content-md-center align-items-md-center" style="height: auto; color: rgb(0, 0, 0); width: auto;">
                                        {{rating}} <FontAwesomeIcon icon="fa-star" />
                                    </h1>
                                </div>
                                <div class="row" style="margin-top: 20px;">
                                    <div class="col text-start">
                                        <h6 class="text-start d-md-flex justify-content-md-center align-items-md-center" style="height: auto;width: auto;margin: 0px;margin-bottom: 0px;">
                                            <span style="color: rgb(0, 0, 0);">MOODS</span>
                                        </h6>
                                    </div>
                                    <p style="font-family: Arial;font-size: 13px;text-align: justify;padding: 5px;padding-top: 0px;padding-bottom: 0px;margin-bottom: 10px;">
                                        <span style="color: rgb(0, 0, 0);">XX% STATEMENT</span>
                                    </p>
                                </div>
                            </div>
                            <div class="col">
                                <div class="row">
                                    <div class="col">
                                        <h1 class="text-start" style="color: rgb(0,0,0);margin: 0px; ">{{title}}</h1>
                                        <h3 class="text-start" style="color: rgb(109,109,109);margin: 0px;margin-bottom: 15px;">{{authors}}
                                        </h3> </div>
                                </div>
                                <div class="row">
                                    <div class="col">
                                        <h6 class="text-start" style="color: rgb(194,194,194);margin: 0px;margin-bottom: 15px;">{{genres}}</h6> </div>
                                </div>
                                <div class="row">
                                    <div class="col" style="height: 311px;">
                                        <h6 class="text-start" style="color: rgb(0,0,0);margin: 0px;margin-bottom: 15px;">SYNOPSIS</h6>
                                        <p class="text-justify" style="font-family: Arial;color: rgb(0,0,0);font-size: 18px;height: 80%; text-align: justify;"> {{description}} </p>
                                    </div>
                                </div>
                            </div>
                        </div>
                        <div class="row">
                            <div class="col flex-column">
                                <h1 class="text-start" style="margin: 0px;margin-bottom: 15px;"><span
                                    style="color: rgb(0, 0, 0);">reviews</span></h1>
                                <div v-if="review.length != 0">
                                    <Review v-for="review in review" :text="review"/>
                                </div>
                                <p style="font-family: Arial;color: rgb(0,0,0);font-size: 18px;text-align: justify;" v-else> 
                                    No available reviews.
                                </p>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </body>
</template>

<script lang="js">
import { defineComponent } from 'vue'
import WhiteHeader from '../components/WhiteHeader.vue'
import Review from '../components/Review.vue'
import axios from 'axios'
import router from '../router'

export default defineComponent({
    name: 'Book',
    data() {
        return {
            author: [],
            authors:"",
            book_format:[],
            description:"",
            genre:[],
            genres:"",
            cover_img:"",
            title:"",
            isbn:"",
            page_count: 0,
            rating:0,
            review_count:0,
            price:0,
            sensitivity: [],
            pacing:"",
            buzzwords:[],
            mood:[],
            mood_percentage:[],
            moods:"",
            review:[]
      }
    },
    components: {
        WhiteHeader,
        Review
    },
    setup() {
        return {}
    },
    async created(){
        await axios.get('http://localhost:8080/book/' + this.$route.params.id).then((res) =>{
            console.log(res.data);
            this.author = res.data.author
            this.book_format = res.data.book_format
            this.description = res.data.description
            this.genre = res.data.genre
            this.cover_img = res.data.cover_img
            this.title = res.data.title
            this.isbn = res.data.isbn
            this.page_count = res.data.page_count
            this.rating = res.data.rating
            this.review_count = res.data.review_count
            this.price = res.data.price
            this.sensitivity = res.data.sensitivity
            this.pacing = res.data.pacing
            this.buzzwords = res.data.buzzwords
            this.mood = res.data.mood
            this.mood_percentage = res.data.mood_percentage
            this.review = res.data.review

            this.authors = this.author.join(", ");
            this.genres = this.genre.join(", ");

            for (var i = 0; i < this.mood_percentage.length; i++) {
                var number = this.mood_percentage[i].split(":")[1];
                number = number.split(",")[0];
                console.log(number);
                number = parseInt(number)*100;
                if(number != 0){
                    this.moods += this.mood_percentage[i].split(":")[0] + " " + number .toString() + "%\n";
                }
                console.log(this.moods);
            }

        });

        

    }
})

</script>