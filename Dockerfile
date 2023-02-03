FROM quay.io/rhmessagingqe/yacfg:0.9.3
COPY profiles /data/profiles
COPY templates /data/templates

ENV YACFG_TEMPLATES=/data/templates
ENV YACFG_PROFILES=/data/profiles