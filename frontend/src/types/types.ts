export interface Campsite {
  name: string;
  type: string;
  accessible: boolean;
}

export interface Location {
  facility_name: string;
  description: string;
  latitude: number;
  longitude: number;
  reservable: boolean;
  image_url: string;
  campsites: number;
  reservation_url: string;
}

export interface CampingDataResponse {
  locations: Location[];
}

export interface ResultsPageProps {
  city: string;
}

export interface LandingPageProps {
  onSearch: (city: string) => void;
}