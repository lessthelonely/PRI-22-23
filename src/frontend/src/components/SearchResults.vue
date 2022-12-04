<template>
    <div class="card" style="color: rgb(0,0,0); width: 100%; margin-bottom: 15px;">
        <div class="card-body" style="">
            <div class="col-12" style="margin-right: 0px;">
                <div class="row">
                    <div class="col-8" style="margin-right: 25px;">
                        <div class="row" style="align-content: start;">
                            <p class="flex-column justify-content-md-end" style="font-size: 10px; margin-bottom: 15px; width: 100%; color: rgb(71, 67, 67); text-align: left;">
                                <em>
                                    This one is {{buzzword}} {{mood}}.
                                </em>
                            </p>
                            <h1 style="margin-bottom: 0px; font-family: Cabin; text-transform: uppercase; text-align: left;">
                                <em>{{ book.title }}</em>
                            </h1>
                            <h5 class="text-muted mb-2"
                                style="font-family: Cabin; text-transform: uppercase; text-align: justify; font-weight: 600;">
                                {{ authors }}</h5>
                            <p style="font-size: 18px;height: 200px;margin-bottom: 10px;width: 100%; text-align: justify;margin-top: 20px;">
                                <span style="color: rgb(30, 25, 21); text-align: justify;">
                                    {{ description }}
                                    <button id="button-search" @click="bookPage">[MORE]</button>
                                </span>
                            </p>
                        </div>
                    </div>
                    <div style="width: 30%;">
                        <img v-bind:src="book.cover_img" style="width:100%; box-shadow: 2px 2px 9px 2px rgb(0 0 0 / 26%); float: right;" />
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script lang="js" >
import { defineComponent } from 'vue';
import router from '../router';


export default defineComponent({
    name: 'SearchResults',
    props: ['book'],
    components: {},
    data() {
        return {
            authors:"",
            description:"",
            buzzword: "",
            moods:[],
            mood: ""
        }
    },
    setup() {
        return {};
    },
    created() {
        this.authors = this.book.author.join(", ");
        if (this.book.description.split(/[\\?|\\.|!]/).length > 2){
            this.description = this.book.description.split(/[\\?|\\.|!]/)[0] + "." + this.book.description.split(/[\\?|\\.|!]/)[1] + ".";
        } else {
            this.description = this.book.description;
        }

        if(this.book.buzzwords!=null){
            var randomBuzzword1 = this.between(0, this.book.buzzwords.length);
            this.buzzword = this.book.buzzwords[randomBuzzword1];
        }

        if(this.book.mood_percentage != "[]"){
            for(var i=0; i<this.book.mood_percentage.length; i++){
            var temp_array = this.book.mood_percentage[i].split(":");
            var temp_number=0;
            if(i==this.book.mood_percentage.length-1){
                    temp_number = temp_array[1].split("]")[0];
                    temp_number=Math.ceil(temp_number*100);
            }
            else{
                temp_number=Math.ceil(temp_array[1]*100);
            }
            if(temp_number != 0){
                    if(i==0){
                        this.moods.push(temp_number + "% " + (this.book.mood_percentage[i].split(":")[0]).split("['")[1].split("'")[0]);
                    }
                    else{
                        this.moods.push(temp_number + "% " + (this.book.mood_percentage[i].split(":")[0]).split("'")[1]);
                    }
            }
            }
        var randomMood = this.between(0, this.book.mood_percentage.length);
        var moodText = this.moods[randomMood];
        moodText = moodText.split(' ');
        this.mood = " and "+ moodText[0] + " of readers felt " + moodText[1];
    }

        
    
    },
    methods: {
        bookPage() {
            window.location.href = "/book/" + this.book.id;
        },

        between(min, max) {  
            return Math.floor( Math.random() * (max - min) + min);
        }
    }

});
</script>

