<template>
    <TransparentHeader />

    <body id="page-top" data-bs-spy="scroll" data-bs-target="#mainNav" data-bs-offset="77"
        style="display: block; width: 100%;">
        <header
            style="background-image:url('https://media.discordapp.net/attachments/1042104897866301470/1046865776814071808/background.png?width=1178&height=662') center / cover no-repeat; ">
            <div class="intro-body row" id="picture-1">
                <div class="col" style="display: flex; flex-direction: column; flex-wrap: nowrap; align-content: center; justify-content: center; align-items: center;">
                    <h1 class="brand-heading" style="width: 100%;">
                        <img src="../assets/images/logo.png" style="width: 65%;">
                    </h1>
                    <h4 class="intro-text" style="font-family: Cabin;">
                        We're not like other girls, we
                        <em>like books</em>.
                    </h4>
                    <a class="btn btn-link btn-circle" role="button" href="#about">
                        <FontAwesomeIcon icon="angle-double-down"  />
                    </a>
                </div>
            </div>
        </header>
        <section class="text-center content-section" id="about">
            <div class="container">
                <div class="row">
                    <div class="col-lg-8 mx-auto" style="font-family: Cabin;">
                        <h2 class="heading">ABOUT</h2>
                        <p style="font-family: Arial;">
                            <em>Reading is hard.</em> No, we mean it literally.<br>
                        </p>
                        <p style="font-family: Arial;">
                            This is why a <em>very </em>competent team has created
                            NOVELideas, which exists to make reading as easy as possible: one doesn't even have to know
                            <em>what&nbsp;</em>they're looking for, only that they're looking for <em>something</em>!
                        </p>
                        <p style="font-family: Arial;">
                            All you have to do is to want to find a new book, and it can be
                            as specific or as vague as you prefer - but what are you doing reading this still? Go try
                            it!
                        </p>
                    </div>
                </div>
            </div>
        </section>
        <section class="text-center download-section content-section" id="picture-2">
            <div class="col" style="height: 300px; display: flex; flex-direction: column; flex-wrap: nowrap; align-content: center; justify-content: center; align-items: center;"></div>
        </section>
        <section class="text-center content-section" id="contact">
            <div class="container">
                <div class="row">
                    <div class="col-lg-8 mx-auto">
                        <h2 class="heading">Contact us</h2>
                        <p style="font-family: Arial;">
                            We really want you to contact us, so use the following links that
                            definitely work!<br>We wouldn't add buttons just because, yeah... totally!
                        </p>
                        <ul class="list-inline banner-social-buttons">
                            <li class="list-inline-item">
                                <button class="btn btn-primary btn-lg btn-default" type="button">
                                    <a class="nav-link" href="mailto:up201906232@up.pt">
                                        E-mail
                                    </a>
                                </button>
                            </li>
                            <li class="list-inline-item">
                                <button class="btn btn-primary btn-lg btn-default" type="button">
                                    <a class="nav-link" href="https://github.com/lessthelonely/PRI-22-23">
                                        Github
                                    </a>
                                </button>
                            </li>
                        </ul>
                    </div>
                </div>
            </div>
        </section>
        <div class="map-clean"></div>
        <footer>
            <div class="container text-center">
                <p style="font-size: 11px;">Copyright ©&nbsp;NOVELIDEAS 2022</p>
            </div>
        </footer>
    </body>
</template>

<script lang="js">
import { defineComponent } from 'vue';
import TransparentHeader from '../components/TransparentHeader.vue';

export default defineComponent({
    name: 'Home',
    components: {
        TransparentHeader
    }
});
</script>