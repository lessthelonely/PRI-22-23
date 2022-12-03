<template>
    <div class='col advanced-filter' :id="this.name" style='margin-top: 10px; display: flex; justify-content: center; align-items: center; align-content: center;'>
        <select class='filter-select' placeholder='Attribute' style='font-family: Cabin; padding: 10px;'>
            <option value='author'>Author</option>
            <option value='book_format'>Format</option>
            <option value='ISBN'>ISBN</option>
            <option value='page_count'>Page Count</option>
            <option value='rating'>Rating</option>
            <option value='review_count'>Review Count</option>
            <option value='title'>Title</option>
            <option value='price'>Price</option>
            <option value='sensitivity'>Sensitivity</option>
            <option value='pacing'>Pacing</option>
            <option value='buzzwords'>Buzzwords</option>
            <option value='mood'>Moods</option>
        </select>
        <input class='filter-input' type='text' style='margin-left: 15px; font-family: Cabin; padding: 10px;' />
        <button v-if="this.name != 'advanced-filter-1'" id='remove-button' style='margin-left: 15px; width: 50px; height: 40px; align-items: center; display: flex; justify-content: center; align-content: center; flex-direction: column; flex-wrap: nowrap;' @click='removeFilter'>
            <FontAwesomeIcon icon="fa-minus" />
        </button>
    </div>
</template>

<script>
import { defineComponent } from 'vue';

export default defineComponent({
    name: 'AdvancedFilter',

    props: {
        name: {
            type: String,
            required: true,
        },
    },

    methods: {
        removeFilter() {
            document.getElementById(this.name).remove();
        }
    }
});
</script>