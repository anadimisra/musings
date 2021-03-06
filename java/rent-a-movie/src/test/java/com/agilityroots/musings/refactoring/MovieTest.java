package com.agilityroots.musings.refactoring;

import org.junit.Test;

import static org.assertj.core.api.Assertions.assertThat;

public class MovieTest {


    @Test
    public void testRentalForNewRelease() {
        Movie movie = new Movie("Some Moview", new NewReleasePrice());

        double charge = movie.getCharge(2);

        assertThat(charge).isEqualTo(6.0);
    }

    @Test
    public void testRentalForRegularMovie() {
        Movie movie = new Movie("Some Moview", new RegularPrice());

        double charge = movie.getCharge(2);

        assertThat(charge).isEqualTo(2.0);
    }

    @Test
    public void testRentalForRegularMovieMoreThanTwoDays() {
        Movie movie = new Movie("Some Moview", new RegularPrice());

        double charge = movie.getCharge(3);

        assertThat(charge).isEqualTo(3.5);
    }

    @Test
    public void testRentalForChildrensMovie() {
        Movie movie = new Movie("Some Moview", new ChildrensPrice());

        double charge = movie.getCharge(2);

        assertThat(charge).isEqualTo(1.5);
    }

    @Test
    public void testRentalForChildrenMovieMoreThanThreeDays() {
        Movie movie = new Movie("Some Moview", new ChildrensPrice());

        double charge = movie.getCharge(4);

        assertThat(charge).isEqualTo(3.0);
    }

    @Test
    public void testFrequentRenterPointsForNewReleases() {
        Movie movie = new Movie("Some Moview", new NewReleasePrice());

        int frequentRenterPoints = movie.getFrequentRenterPoints(2);

        assertThat(frequentRenterPoints).isEqualTo(2);
    }

    @Test
    public void testFrequentRenterPointsForOtherReleases() {
        Movie movie = new Movie("Some Moview", new RegularPrice());

        int frequentRenterPoints = movie.getFrequentRenterPoints(2);

        assertThat(frequentRenterPoints).isEqualTo(1);
    }
}
