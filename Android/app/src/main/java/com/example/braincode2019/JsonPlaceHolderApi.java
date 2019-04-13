package com.example.braincode2019;

import java.util.List;

import retrofit2.Call;
import retrofit2.http.GET;
import retrofit2.http.Query;

public interface JsonPlaceHolderApi {
    @GET("test")
    Call<List<JsonData>> getPost(@Query("1") int dlugosc,
                                 @Query("2") int szerokosc);

    //http://localhost:8000/GPS_GET?dlugosc=100&szerokosc=200
    //http://192.168.43.28:8000/test?1=3&2=5
    @GET("test")
    Call<List<JsonGeo>> getGeo(@Query("1") double dlugosc,
                               @Query("2") double szerokosc);
}
