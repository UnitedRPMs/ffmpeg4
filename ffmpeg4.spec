%global realname ffmpeg

%undefine _debuginfo_subpackages
%undefine _debugsource_packages

%global _lto_cflags %{nil}


%if 0%{?fedora} >= 25
# OpenCV 3.X has an overlinking issue - unsuitable for core libraries
# Reported as https://github.com/opencv/opencv/issues/7001
%global _without_opencv   1
%endif

%if 0%{?rhel}
%global _without_frei0r   1
%global _without_vpx      1
%bcond_without opencv
%else
%bcond_with opencv
%endif


# Wait, will be enabled the next update
# https://git.ffmpeg.org/gitweb/ffmpeg.git/blob/81d3d7dd44acc7ae7c57e99176d1d428fb40c353:/Changelog
%bcond_with dav1d

%bcond_with davs2
%bcond_with xavs2

%bcond_with libfdk-aac
# We need to test it
# fdk-aac-free https://bugzilla.redhat.com/show_bug.cgi?id=1501522 doesn't support 
# variable bitrate (`-q` flag)

# Globals for git repository
%global commit0 7e0d640edf6c3eee1816b105c2f7498c4f948e74
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global gver .git%{shortcommit0}


Summary:        Digital VCR and streaming server
Name:           ffmpeg4
Version:        4.4.1
Release:        1%{?dist}
%if 0%{?_with_amr:1}
License:        GPLv3+
%else
License:        GPLv2+
%endif
URL:            http://ffmpeg.org/
Source0:	https://git.ffmpeg.org/gitweb/ffmpeg.git/snapshot/%{commit0}.tar.gz#/%{realname}-%{shortcommit0}.tar.gz
# Backport of http://git.videolan.org/?p=ffmpeg.git;a=commitdiff;h=a606f27f4c610708fa96e35eed7b7537d3d8f712 thanks to Nicolas George
Source1:	ffmpeg4.sh
Source2:	ffmpeg4.conf
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
BuildRequires:  bzip2-devel
%{?_with_faac:BuildRequires: faac-devel}
%{?_with_fdk_aac:BuildRequires: fdk-aac-devel}
%{?_with_flite:BuildRequires: flite-devel}
BuildRequires:  fontconfig-devel
BuildRequires:  freetype-devel
%{!?_without_frei0r:BuildRequires: frei0r-devel}
%{?_with_gme:BuildRequires: game-music-emu-devel}
BuildRequires:  gnutls-devel
BuildRequires:  gsm-devel
%{?_with_ilbc:BuildRequires: ilbc-devel}
BuildRequires:  lame-devel >= 3.98.3
%{!?_without_jack:BuildRequires: jack-audio-connection-kit-devel}
%{!?_without_ladspa:BuildRequires: ladspa-devel}
BuildRequires:  libass-devel
BuildRequires:  libbluray-devel
%{?_with_bs2b:BuildRequires: libbs2b-devel}
%{?_with_caca:BuildRequires: libcaca-devel}
%{!?_without_cdio:BuildRequires: libcdio-paranoia-devel}
%{?_with_chromaprint:BuildRequires: libchromaprint-devel}
#libcrystalhd is currently broken
%{?_with_crystalhd:BuildRequires: libcrystalhd-devel}
%if 0%{?_with_ieee1394}
BuildRequires:  libavc1394-devel
BuildRequires:  libdc1394-devel
BuildRequires:  libiec61883-devel
%endif
BuildRequires:  libgcrypt-devel
BuildRequires:  libGL-devel
BuildRequires:  libmodplug-devel
%{?_with_rtmp:BuildRequires: librtmp-devel}
%{?_with_smb:BuildRequires: libsmbclient-devel}
%{?_with_ssh:BuildRequires: libssh-devel}
BuildRequires:  libtheora-devel
BuildRequires:  libv4l-devel
BuildRequires:  libvdpau-devel
BuildRequires:  libvorbis-devel
%{?!_without_vpx:BuildRequires: libvpx-devel >= 0.9.1}
%ifarch %{ix86} x86_64
BuildRequires:  libmfx-devel
BuildRequires:  libXvMC-devel
BuildRequires:  libva-devel >= 0.31.0
BuildRequires:  yasm
%endif
%{?_with_webp:BuildRequires: libwebp-devel}
%{?_with_netcdf:BuildRequires: netcdf-devel}
%{!?_without_nvenc:BuildRequires: nvenc-devel nv-codec-headers >= 9.0.18.2}
%{?_with_amr:BuildRequires: opencore-amr-devel vo-amrwbenc-devel}
%{!?_without_openal:BuildRequires: openal-soft-devel}
%if 0%{!?_without_opencl:1}
BuildRequires:  opencl-headers ocl-icd-devel
Recommends:     opencl-icd
%endif
%{!?_without_opencv:BuildRequires: opencv-devel}
BuildRequires:  openjpeg2-devel
BuildRequires:  openjpeg-devel
BuildRequires:  opus-devel
%{!?_without_pulse:BuildRequires: pulseaudio-libs-devel}
%if 0%{?fedora} >= 35
BuildRequires:	libpulsecommon-15.0.so
%endif
BuildRequires:  perl(Pod::Man)
%{?_with_rubberband:BuildRequires: rubberband-devel}
BuildRequires:  SDL2-devel
%{?_with_snappy:BuildRequires: snappy-devel}
BuildRequires:  soxr-devel
BuildRequires:  speex-devel
BuildRequires:  subversion
%{?_with_tesseract:BuildRequires: tesseract-devel}
#BuildRequires:  texi2html
BuildRequires:  texinfo
%{?_with_twolame:BuildRequires: twolame-devel}
%{?_with_wavpack:BuildRequires: wavpack-devel}
%{!?_without_x264:BuildRequires: x264-devel >= 1:0.163}
%{!?_without_x265:BuildRequires: x265-devel >= 3.5}
%{!?_without_xvid:BuildRequires: xvidcore-devel}
BuildRequires:  zlib-devel
%{?_with_zmq:BuildRequires: zeromq-devel}
%{?_with_zvbi:BuildRequires: zvbi-devel}
BuildRequires:  libxcb-devel libxcb
# New support
BuildRequires:	librockchip-devel librockchip-vpu-devel
BuildRequires:	lilv-devel
BuildRequires:	libdrm-devel
BuildRequires:	openh264-devel >= 2.1.1
BuildRequires:	kvazaar-devel >= 2.0.0
BuildRequires:	libmysofa-devel >= 1.2
BuildRequires:	shine-devel
BuildRequires:	vid.stab-devel >= 1.1.0
BuildRequires:	libvmaf-devel 
BuildRequires:	zvbi-devel
BuildRequires:	alsa-lib-devel
BuildRequires:	svt-av1-devel
%if 0%{?fedora} >= 31
BuildRequires:	libopenmpt-devel
%endif
%if 0%{?fedora} >= 35
BuildRequires:  libaom-devel >= 3.2.0
%else
BuildRequires:  libaom-devel
%endif 
BuildRequires:	vapoursynth-devel
BuildRequires:	srt-devel
%if 0%{?fedora} >= 34
BuildRequires:	rav1e-devel
%endif
%if %{without dav1d}
%if 0%{?fedora} >= 34
BuildRequires:	libdav1d-devel >= 0.8.0
%else
BuildRequires:	libdav1d-devel >= 0.5.2
%endif
%endif
%if %{without davs2}
BuildRequires: davs2-devel >= 1.5.115
%endif
%if %{without xavs2}
BuildRequires: xavs2-devel >= 1.2.77
%endif
%if %{without libfdk-aac}
BuildRequires: fdk-aac-free-devel >= 2.0.0
%endif
BuildRequires: cmrt-devel
BuildRequires: libva-devel
BuildRequires: libva-intel-hybrid-driver
BuildRequires: libva-intel-driver
BuildRequires: vulkan-loader vulkan-loader-devel vulkan-headers vulkan-loader-compat-devel
BuildRequires: glslang glslang-devel 
#BuildRequires: lensfun-devel
%if 0%{?fedora} >= 33
BuildRequires: libsmbclient-devel >= 4.13.3
%endif
BuildRequires: libxml2-devel

%description
FFmpeg is a complete and free Internet live audio and video
broadcasting solution for Linux/Unix. It also includes a digital
VCR. It can encode in real time in many formats including MPEG1 audio
and video, MPEG4, h263, ac3, asf, avi, real, mjpeg, and flash.

%package        libs
Summary:        Libraries for %{name}
Supplements:	firefox <= 60

%description    libs
FFmpeg is a complete and free Internet live audio and video
broadcasting solution for Linux/Unix. It also includes a digital
VCR. It can encode in real time in many formats including MPEG1 audio
and video, MPEG4, h263, ac3, asf, avi, real, mjpeg, and flash.
This package contains the libraries for %{name}

%package     -n libavdevice4
Summary:        Special devices muxing/demuxing library

%description -n libavdevice4
Libavdevice is a complementary library to libavf "libavformat". It provides
various "special" platform-specific muxers and demuxers, e.g. for grabbing
devices, audio capture and playback etc.

%package        devel
Summary:        Development package for %{name}
Requires:       %{name}-libs%{_isa} = %{version}-%{release}
Requires:       libavdevice4%{_isa} = %{version}-%{release}
Requires:       pkgconfig
Requires:       libxcb
Conflicts:	ffmpeg-devel

%description    devel
FFmpeg is a complete and free Internet live audio and video
broadcasting solution for Linux/Unix. It also includes a digital
VCR. It can encode in real time in many formats including MPEG1 audio
and video, MPEG4, h263, ac3, asf, avi, real, mjpeg, and flash.
This package contains development files for %{name}

%package        bin
Summary:        symlink for %{name}
Requires:       %{name}-libs%{_isa} = %{version}-%{release}
Requires:       libavdevice4%{_isa} = %{version}-%{release}
Conflicts:	ffmpeg
%description    bin
FFmpeg is a complete and free Internet live audio and video
broadcasting solution for Linux/Unix. It also includes a digital
VCR. It can encode in real time in many formats including MPEG1 audio
and video, MPEG4, h263, ac3, asf, avi, real, mjpeg, and flash.
This package contains development files for %{name}

%global ff_configure \
./configure \\\
    --prefix=%{_prefix} \\\
    --bindir=%{_bindir}/%{name} \\\
    --datadir=%{_datadir}/%{name} \\\
    --docdir=%{_docdir}/%{name} \\\
    --incdir=%{_includedir}/%{name} \\\
    --libdir=%{_libdir} \\\
    --mandir=%{_mandir}/%{name} \\\
    --pkgconfigdir=%{_datadir}/pkgconfig \\\
    --optflags="%{optflags}" \\\
    --extra-ldflags="%{?__global_ldflags}" \\\
    %{?_with_amr:--enable-libopencore-amrnb --enable-libopencore-amrwb --enable-libvo-amrwbenc --enable-version3} \\\
    --enable-bzlib \\\
    --enable-libdrm \\\
    %{?_with_chromaprint:--enable-chromaprint} \\\
    %{!?_with_crystalhd:--disable-crystalhd} \\\
    --enable-fontconfig \\\
    %{!?_without_frei0r:--enable-frei0r} \\\
    --enable-gcrypt \\\
    %{?_with_gmp:--enable-gmp --enable-version3} \\\
    --enable-gnutls \\\
    %{!?_without_ladspa:--enable-ladspa} \\\
    --enable-libass \\\
    --enable-libbluray \\\
    %{?_with_bs2b:--enable-libbs2b} \\\
    %{?_with_caca:--enable-libcaca} \\\
    %{!?_without_cdio:--enable-libcdio} \\\
    %{?_with_ieee1394:--enable-libdc1394 --enable-libiec61883} \\\
    %{?_with_faac:--enable-libfaac --enable-nonfree} \\\
    %{?_with_flite:--enable-libflite} \\\
    --enable-libjack \\\
    --enable-libfreetype \\\
    --enable-libfribidi \\\
    %{?_with_gme:--enable-libgme} \\\
    --enable-libgsm \\\
    %{?_with_ilbc:--enable-libilbc} \\\
    --enable-libmp3lame \\\
    --enable-libkvazaar \\\
    %{?_with_netcdf:--enable-netcdf} \\\
    %{!?_without_nvenc:--enable-nvenc --extra-cflags="-I%{_includedir}/nvenc"} \\\
    %{!?_without_openal:--enable-openal} \\\
    %{!?_without_opencl:--enable-opencl} \\\
    %{!?_without_opencv:--enable-libopencv} \\\
    --enable-libopenh264 \\\
    --enable-libmysofa \\\
    --enable-libshine \\\
    --enable-libzvbi \\\
    --enable-libvidstab \\\
    --enable-libaom \\\
    --enable-libmfx \\\
    --enable-vapoursynth \\\
    %{!?_without_opengl:--enable-opengl} \\\
    --enable-libopenjpeg \\\
    --enable-libopus \\\
    %{!?_without_pulse:--enable-libpulse} \\\
    %{?_with_rtmp:--enable-librtmp} \\\
    %{?_with_rubberband:--enable-librubberband} \\\
    %{?_with_snappy:--enable-libsnappy} \\\
    --enable-libsoxr \\\
    --enable-libspeex \\\
    %{?_with_ssh:--enable-libssh} \\\
    %{?_with_tesseract:--enable-libtesseract} \\\
    --enable-libtheora \\\
    %{?_with_twolame:--enable-libtwolame} \\\
    --enable-libvorbis \\\
    --enable-libv4l2 \\\
    %{!?_without_vpx:--enable-libvpx} \\\
    %{?_with_webp:--enable-libwebp} \\\
    %{!?_without_x264:--enable-libx264} \\\
    %{!?_without_x265:--enable-libx265} \\\
    %{!?_without_xvid:--enable-libxvid} \\\
    %{?_with_zmq:--enable-libzmq} \\\
    %{?_with_zvbi:--enable-libzvbi} \\\
    --enable-avfilter \\\
    --enable-postproc \\\
    --enable-pthreads \\\
    --disable-static \\\
    --enable-shared \\\
    --enable-gpl \\\
    --disable-debug \\\
    --disable-stripping \\\
    --enable-rdft \\\
    --enable-pixelutils \\\
    --enable-sdl2 \\\
    --enable-swscale \\\
    --enable-vulkan \\\
    --enable-rkmpp --enable-version3 \\\
    --enable-lv2 \\\
    --enable-libxml2 \\\
    --enable-libsvtav1 \\\
    --enable-libglslang


    
    
# --disable-error-resilience \\\ broken in 4.4
# --enable-liblensfun \\\ broken in 4.4
# --enable-pic \\\ bad performance  
#--arch=%%{_target_cpu} \\\
# use optimizations for current CI CPU, useless 'cause not universal    
#--enable-x11grab \\\
# was deleted as legacy
# https://www.ffmpeg.org/ffmpeg-devices.html#x11grab


%prep
%autosetup -n %{realname}-%{shortcommit0} -p1

# fix -O3 -g in host_cflags
mkdir -p _doc/examples
cp -pr doc/examples/{*.c,Makefile,README} _doc/examples/

# fix glslang compatibility (We need test it; but our glslang don't need it)
# sed -i "s|#include <glslang/Include/revision.h>||" libavfilter/glslang.cpp (We have a patch)
#sed -i "s|-lOSDependent||" configure
#sed -i "s|-lOGLCompiler||" configure

# fix error in vulkan pkgconfig (We need previlegies and touch the official package; we don't need it; solved with our vulkan-loader-compat-devel)
# sed -i 's|vulkan64|vulkan|g' /usr/lib64/pkgconfig/vulkan.pc


%build
#     --shlibdir=%{_libdir}/%{name} \

%{ff_configure}\
    --shlibdir=%{_libdir} \
%if 0%{?ffmpegsuffix:1}
    --build-suffix=%{ffmpegsuffix} \
    --disable-doc \
    --disable-ffmpeg --disable-ffplay --disable-ffprobe --disable-ffserver \
%else
%ifarch %{ix86}
    --cpu=%{_target_cpu} \
%endif
%ifarch %{ix86} x86_64 ppc ppc64
    --enable-runtime-cpudetect \
%endif
%ifarch ppc
    --cpu=g3 \
    --enable-pic \
%endif
%ifarch ppc64
    --cpu=g5 \
    --enable-pic \
%endif
%ifarch %{arm}
    --disable-runtime-cpudetect --arch=arm \
%ifarch armv6hl
    --cpu=armv6 \
%else
    --enable-thumb \
%endif
%ifarch armv7hl armv7hnl
    --cpu=armv7-a \
    --enable-vfpv3 \
    --enable-thumb \
%endif
%ifarch armv7hnl
    --enable-neon \
%endif
%ifarch armv7hl
    --disable-neon \
%endif
%endif
%endif

%make_build V=0 AM_DEFAULT_VERBOSITY=0
make documentation V=0
make alltools V=0 AM_DEFAULT_VERBOSITY=0

%install
%make_install V=0
rm -r %{buildroot}%{_datadir}/%{name}/examples
%if 0%{!?ffmpegsuffix:1}
install -pm755 tools/qt-faststart %{buildroot}/%{_bindir}/%{name}
%endif

ln -sf %{_bindir}/%{name}/ffmpeg %{buildroot}/%{_bindir}/ffmpeg
ln -sf %{_bindir}/%{name}/ffplay %{buildroot}/%{_bindir}/ffplay
ln -sf %{_bindir}/%{name}/ffprobe %{buildroot}/%{_bindir}/ffprobe
ln -sf %{_bindir}/%{name}/qt-faststart %{buildroot}/%{_bindir}/qt-faststart

# Install profile and ld.so.config files
install -Dm755 %{S:1} "%{buildroot}/etc/profile.d/ffmpeg4.sh"
install -Dm644 %{S:2} "%{buildroot}/etc/ld.so.conf.d/ffmpeg4.conf"

%post libs -p /sbin/ldconfig

%postun libs -p /sbin/ldconfig

%post -n libavdevice4 -p /sbin/ldconfig

%postun -n libavdevice4 -p /sbin/ldconfig

%if 0%{!?ffmpegsuffix:1}
%files
%doc COPYING.* CREDITS README.md 
%{_bindir}/%{name}/ffmpeg
%{_bindir}/%{name}/ffplay
%{_bindir}/%{name}/ffprobe
%{_bindir}/%{name}/qt-faststart
%{_mandir}/%{name}/man1/ffmpeg*.1*
%{_mandir}/%{name}/man1/ffplay*.1*
%{_mandir}/%{name}/man1/ffprobe*.1*
%{_datadir}/%{name}
%{_sysconfdir}/profile.d/%{name}.sh
%endif

%files libs
%{_libdir}/lib*.so.*
#exclude %{_libdir}/libavdevice.so.*
%{_mandir}/%{name}/man3/lib*.3.gz
#exclude %{_mandir}/%{name}/man3/libavdevice.3*
%{_sysconfdir}/ld.so.conf.d/%{name}.conf

%files -n libavdevice4
%{_libdir}/libavdevice.so.*
%{_mandir}/%{name}/man3/libavdevice.3*

%files devel
%doc MAINTAINERS doc/APIchanges doc/*.txt
%doc _doc/examples
%doc %{_docdir}/%{name}/*.html
%{_includedir}/%{name}
%{_datadir}/pkgconfig/lib*.pc
%{_libdir}/lib*.so

%files bin
%{_bindir}/ffmpeg
%{_bindir}/ffplay
%{_bindir}/ffprobe
%{_bindir}/qt-faststart

%changelog

* Sat Jan 15 2022 Unitedrpms Project <unitedrpms AT protonmail DOT com> 4.4.1-1
- Initial build
