%define debug_package %{nil}

%define name		pyobd2
%define Summary         OBD-II compliant car diagnostic tool.
%define Summary_hu      OBD-II autodiagnosztikai eszköz
%define sourcetype      tar.xz
%define version         20230220

Name: 		%name
Summary: 	%Summary
Summary(hu): 	%Summary_hu
Version:	%version
Release:  	%mkrel 2
License: 	GPL2
Distribution:	blackPanther OS
Vendor:    	blackPanther Europe
Packager:  	Karoly Barcza <kbarcza@blackpanther.hu>
Group: 		Utility
Source0:	%name-%version.%sourcetype
BuildArch:	noarch
BuildRequires:	python3
Requires: 	python3-wxpython4
Requires: 	python3-serial 
Requires: 	python3-configparser

%description
Is a OBD-II compliant car diagnostic tool.


%files
%defattr(-,root,root)
%doc README.md COPYING
%_bindir/%name
%_datadir/%name/
%_datadir/applications/%name.desktop
%_iconsdir/*.png
%_iconsdir/*/*.png

%prep
%setup -q -n %name

%build

%install
mkdir -p %buildroot/%_datadir/%name
cp *.py %buildroot/%_datadir/%name/
cp *.png %buildroot/%_datadir/%name/
install %name %buildroot/%_datadir/%name/%name
mkdir -p %buildroot/%_bindir/
ln -sf %_datadir/%name/%name %buildroot/%_bindir/%name

rm -rf %buildroot/%_datadir/%name/debian
rm -rf %buildroot/%_datadir/pixmaps
%define  nameicon %name.png
mkdir -p -m755 %{buildroot}{%_liconsdir,%_iconsdir,%_miconsdir}
convert -scale 64x64 %{nameicon} %{buildroot}/%{_liconsdir}/%{name}.png
convert -scale 48x48 %{nameicon} %{buildroot}/%{_iconsdir}/%{name}.png
convert -scale 32x32 %{nameicon} %{buildroot}/%{_miconsdir}/%{name}.png
#install -d -m 755 %{buildroot}%{_iconsdir}/hicolor/scalable/apps
#install -m 644 %{name}.svg %{buildroot}%{_iconsdir}/hicolor/scalable/apps/%{name}.svg


rm -rf %{buildroot}%{_datadir}/applications
mkdir -p %{buildroot}%{_datadir}/applications
install -m644 pyobd.desktop %{buildroot}%{_datadir}/applications/%name.desktop

%clean
rm -rf %buildroot

%changelog
* Mon Feb 20 2023 Charles K. Barcza <info@blackpanther.hu> 20230220-2bP
- build package for blackPanther OS v22.x 32/64 bit or ARM
- fix dependency
------------------------------------------------------------------------
* Mon Feb 20 2023 Charles K. Barcza <info@blackpanther.hu> 20230220-1bP
- build package for blackPanther OS v22.x 32/64 bit or ARM
------------------------------------------------------------------------


