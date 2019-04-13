package com.example.braincode2019;

import java.util.List;

import retrofit2.Call;
import retrofit2.http.GET;
import retrofit2.http.Query;

//http://192.168.43.28:8000/GPS_GET?dlugosc=20&szerokosc=50&dzien=MONDAY&godzina=23:04&odleglosc=0
public interface JsonPlaceHolderApi {
    @GET("GPS_GET")
    Call<List<JsonData>> getPost(@Query("dlugosc") double dlugosc,
                                 @Query("szerokosc") double szerokosc);

    //http://localhost:8000/GPS_GET?dlugosc=100&szerokosc=200
    //http://192.168.43.28:8000/test?1=3&2=5
    @GET("test")
    Call<List<JsonGeo>> getGeo(@Query("1") double dlugosc,
                               @Query("2") double szerokosc);
}
