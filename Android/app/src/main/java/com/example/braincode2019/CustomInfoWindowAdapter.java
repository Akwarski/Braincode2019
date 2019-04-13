package com.example.braincode2019;

import android.content.Context;
import android.support.v4.content.ContextCompat;
import android.view.LayoutInflater;
import android.view.View;
import android.widget.TextView;
import android.widget.Toast;

import com.google.android.gms.maps.GoogleMap;
import com.google.android.gms.maps.model.Marker;

public class CustomInfoWindowAdapter implements GoogleMap.InfoWindowAdapter{

    private final View mView;
    private Context context;
    TextView tv;

    public CustomInfoWindowAdapter(View mView) {
        this.mView = mView;
        mView = LayoutInflater.from(context).inflate(R.layout.pop_window, null);
    }

    private void fun(Marker marker, View view){
        String title = marker.getTitle();
        tv.findViewById(R.id.tv);
        tv.setText(title);
    }

    @Override
    public View getInfoWindow(Marker marker) {
        fun(marker, mView);
        return mView;
    }

    @Override
    public View getInfoContents(Marker marker) {
        return mView;
    }
}
