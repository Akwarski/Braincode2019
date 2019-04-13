package com.example.braincode2019;

import android.Manifest;
import android.content.Intent;
import android.content.pm.PackageManager;
import android.location.Location;
import android.location.LocationListener;
import android.location.LocationManager;
import android.os.Build;
import android.provider.Settings;
import android.support.annotation.NonNull;
import android.support.annotation.RequiresApi;
import android.support.v4.app.ActivityCompat;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;

import com.google.android.gms.location.FusedLocationProviderClient;
import com.google.android.gms.location.LocationServices;
import com.google.android.gms.tasks.OnCompleteListener;
import com.google.android.gms.tasks.Task;

import java.util.List;

import retrofit2.Call;
import retrofit2.Callback;
import retrofit2.Response;
import retrofit2.Retrofit;
import retrofit2.converter.gson.GsonConverterFactory;

public class MainActivity extends AppCompatActivity {

    TextView tv1, tv2;
    Button button1, button2;
    private FusedLocationProviderClient fusedLocationProviderClient;
    JsonPlaceHolderApi jsonPlaceHolderApi;
    double dlugosc, szerokosc;
    public static final String API_BASE_URL = "http://192.168.43.28:8000";

    @RequiresApi(api = Build.VERSION_CODES.M)
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        tv1 = findViewById(R.id.myLocation);
        tv2 = findViewById(R.id.deliveryLocation);
        button1 = findViewById(R.id.button1);
        button2 = findViewById(R.id.button2);

        //http://localhost:8000/GPS_GET?dlugosc=100&szerokosc=200
        Retrofit retrofit = new Retrofit.Builder()
                .baseUrl(API_BASE_URL)
                .addConverterFactory(GsonConverterFactory.create())
                .build();

        //JsonData
        jsonPlaceHolderApi = retrofit.create(JsonPlaceHolderApi.class);
        getData();

        //JsonGeo
        //getGeo();


        //Location
        fusedLocationProviderClient = LocationServices.getFusedLocationProviderClient(this);
        button1.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                getLocation();
            }
        });

    }

    public void getData(){
        Call<List<JsonData>> call = jsonPlaceHolderApi.getPost(2,3);

        call.enqueue(new Callback<List<JsonData>>() {
            @Override
            public void onResponse(Call<List<JsonData>> call, Response<List<JsonData>> response) {
                if (!response.isSuccessful()) {
                    tv2.setText(response.code());
                    return;
                }

                List<JsonData> items = response.body();

                for (JsonData item : items) {
                    StringBuilder sb = new StringBuilder();
                    sb.append("type: " + item.getType() + "\n");
                    sb.append("name: " + item.getName() + "\n");
                    sb.append("adress: " + item.getAdress() + "\n");
                    sb.append("post_code: " + item.getPost_code() + "\n");
                    sb.append("city: " + item.getCity() + "\n");
                    sb.append("dlugosc: " + item.getDlugosc() + "\n");
                    sb.append("szerokosc: " + item.getSzerokosc() + "\n");
                    //sb.append("dates: " + item.getDates() + "\n");

                    tv2.append(sb);
                }
            }

            @Override
            public void onFailure(Call<List<JsonData>> call, Throwable t) {
                tv2.setText(t.getMessage());
            }
        });
    }

    public void getGeo(){
        Call<List<JsonGeo>> call = jsonPlaceHolderApi.getGeo(3, 5);

        call.enqueue(new Callback<List<JsonGeo>>() {
            @Override
            public void onResponse(Call<List<JsonGeo>> call, Response<List<JsonGeo>> response) {
                if (!response.isSuccessful()) {
                    tv2.setText(response.code());
                    return;
                }

                List<JsonGeo> geos = response.body();

                for (JsonGeo geo : geos) {
                    StringBuilder sb = new StringBuilder();
                    sb.append("dlugosc: " + geo.getDlugosc() + "\n");
                    sb.append("szerokosc: " + geo.getSzerokosc() + "\n");

                    tv2.append(sb);
                }
            }

            @Override
            public void onFailure(Call<List<JsonGeo>> call, Throwable t) {
                tv2.setText(t.getMessage());
            }
        });
    }

    private void getLocation() {
        if (ActivityCompat.checkSelfPermission(this, Manifest.permission.ACCESS_FINE_LOCATION) != PackageManager.PERMISSION_GRANTED && ActivityCompat.checkSelfPermission(this, Manifest.permission.ACCESS_COARSE_LOCATION) != PackageManager.PERMISSION_GRANTED) {
            return;
        }
        fusedLocationProviderClient.getLastLocation().addOnCompleteListener(new OnCompleteListener<Location>() {
            @Override
            public void onComplete(@NonNull Task<Location> task) {
                if(task.isSuccessful()){
                    Location location = task.getResult();
                    try {
                        tv1.setText("\n" + location.getLatitude() + " " + location.getLongitude());
                        dlugosc = location.getLatitude();
                        szerokosc = location.getLongitude();
                    }catch (IllegalArgumentException e){
                        //tv1.setText("error");
                    }
                }
            }
        });
    }
}