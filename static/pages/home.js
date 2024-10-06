const Home = {
    template : `
        <div id="myCarousel" class="carousel slide carousel-fade" data-bs-ride="carousel" data-bs-pause="false">
            <div class="carousel-indicators">
                <button type="button" data-bs-target="#myCarousel" data-bs-slide-to="0" class="active" aria-current="true" aria-label="Slide 1"></button>
                <button type="button" data-bs-target="#myCarousel" data-bs-slide-to="1" aria-label="Slide 2"></button>
                <button type="button" data-bs-target="#myCarousel" data-bs-slide-to="2" aria-label="Slide 3"></button>
            </div>
            <div class="carousel-inner">
                <div class="carousel-item active">
                    <img src="/static/media/crop_premium_photo-1684341008385-31d2eb4f3afe.jpg" class="d-block w-100" alt="...">
                    <div class="carousel-caption d-none d-md-block">
                        <div style="background-color: rgba(68, 68, 68, 0.5); border-radius:10px;">
                            <h5>Verified Influencers and Sponsors</h5>
                            <p>No more risk of being misled by fake impersonators.</p>
                        </div>
                    </div>
                </div>
                <div class="carousel-item">
                    <img src="/static/media/crop_premium_photo-1684341008757-3b456034e943.jpg" class="d-block w-100" alt="...">
                    <div class="carousel-caption d-none d-md-block">
                        <div style="background-color: rgba(68, 68, 68, 0.5); border-radius:10px;">
                            <h5>Be Found</h5>
                            <p>Get access to a great selection of influencers and sponsors according to your needs.</p>
                        </div>
                    </div>
                </div>
                <div class="carousel-item">
                    <img src="/static/media/crop_beautiful-rendering-dating-app-concept.jpg" class="d-block w-100" alt="...">
                    <div class="carousel-caption d-none d-md-block">
                        <div style="background-color: rgba(68, 68, 68, 0.5); border-radius:10px;">
                            <h5>Increase Your Reach</h5>
                            <p>Improve your visibility with our system that gives you the best matches for your needs.</p>
                        <div>
                    </div>
                </div>
            </div>
        </div>

    `
}

export default Home