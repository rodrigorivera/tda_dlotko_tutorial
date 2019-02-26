/*    This file is part of the Gudhi Library. The Gudhi library
 *    (Geometric Understanding in Higher Dimensions) is a generic C++
 *    library for computational topology.
 *
 *    Author(s):       Pawel Dlotko
 *
 *    Copyright (C) 2018 Swansea University
 *
 *    This program is free software: you can redistribute it and/or modify
 *    it under the terms of the GNU General Public License as published by
 *    the Free Software Foundation, either version 3 of the License, or
 *    (at your option) any later version.
 *
 *    This program is distributed in the hope that it will be useful,
 *    but WITHOUT ANY WARRANTY; without even the implied warranty of
 *    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 *    GNU General Public License for more details.
 *
 *    You should have received a copy of the GNU General Public License
 *    along with this program.  If not, see <http://www.gnu.org/licenses/>.
 */

#include <gudhi/Persistence_landscape.h>
#include <gudhi/reader_utils.h>
#include <gudhi/graph_simplicial_complex.h>
#include <gudhi/Simplex_tree.h>
#include <gudhi/Persistent_cohomology.h>
#include <gudhi/Rips_complex.h>
#include <gudhi/distance_functions.h>

#include <iostream>
#include <vector>
#include <ctime>
#include <algorithm>



/**
 * USE INSTRUCTIONS.
 * Please download the source code of a Gudhi library from the following link: http://gudhi.gforge.inria.fr/
 * Please palce this file, and the attached makefile into example/Persistence_representations
 * Then compile Gudhi using 
 * mkdir build
 * cd build
 * cmake -DWITH_GUDHI_EXAMPLE=ON ..
 * cd /example/Persistence_representations/
 * make
 * ./study_of_random_point_cloud_in_different_dimensions
 * Run it for different parameters below. In particular please change the dimension parameters.
 * Warning... Do not get too high. Those are costly computations, and they may consume all your memory. 
 * 
**/ 



using Point = std::vector<double>;
using Simplex_tree = Gudhi::Simplex_tree<>;
using Filtration_value = Simplex_tree::Filtration_value;
using Rips_complex = Gudhi::rips_complex::Rips_complex<Filtration_value>;

using namespace Gudhi::persistent_cohomology;

using Persistence_landscape = Gudhi::Persistence_representations::Persistence_landscape;

/**
 * This function generate a random point cloud of a cardinality number_of_points in R^dimension.
 * We will do it by sampling points from a random distribution. 
**/ 
std::vector< Point > generate_random_point_cloud_in_given_dimension( unsigned dimension , unsigned number_of_points )
{
	std::default_random_engine generator;
	generator.seed( time(0) );
    std::uniform_real_distribution<double> distribution(0.0,1.0);
	std::vector< std::vector<double> > result;
	result.reserve( number_of_points );
	for ( size_t i = 0 ; i != number_of_points ; ++i )
	{
		Point point;
		point.reserve( dimension );	
		for ( size_t j = 0 ; j != dimension ; ++j )
		{
			point.push_back( distribution(generator) );
		}
		result.push_back( point );
	}	
	return result;
}


/**
 * This function compute distance between a pair if points.
**/ 
double distance_between_points( const Point& first , const Point& second )
{
	assert( first.size() == second.size() );
	double distance = 0;
	for ( size_t i = 0 ; i != first.size() ; ++i )  
	{
		distance += ( first[i]-second[i] )*( first[i]-second[i] );
	}
	distance = sqrt(distance);
	return distance;
}

/**
 * This function first compute average distance between points, and subsequently
 * normalize point cloud so that the average distance between points is 1. 
 * Note that this procedure change the input vector.
**/ 
void normalize_distance_between_points( std::vector< Point >& original_points )
{
	//first compute average distnace between points:
	double average_distance = 0;
	unsigned counter = 0;
	for ( size_t i = 0 ; i != original_points.size() ; ++i )
	{
		for ( size_t j = i+1 ; j != original_points.size() ; ++j ) 
		{
			average_distance += distance_between_points( original_points[i] , original_points[j] );
			counter++;
		}
	}
	average_distance /= counter;
	
	//not normalize all the points:
	for ( size_t pt = 0 ; pt != original_points.size() ; ++pt )
	{
		for ( size_t i = 0 ; i != original_points[pt].size() ; ++i )
		{
			original_points[pt][i] /= average_distance;
		}
	}
}


int main() 
{
	//Please set up here the dimensions form which the point clouds will be sampled. 
	unsigned dimension1 = 5;
	unsigned dimension2 = 3;
	
	//Please set up here the dimension of persistence homology you are going to use:
	unsigned dimension_of_persistence = 1;
	
	//Please set up here the number of point clouds to be sampled from each dimension.
	unsigned number_of_samples = 100;
	
	//Please set up here the number of points to be samped in each sampling.
	unsigned number_of_points_to_sample = 100;
	
	//Please set up here the treshold for the Rips complex computations.
	double threshold = 1;
	
	std::vector< Persistence_landscape* > persistence_of_point_cloud_in_dimension_1;
	std::vector< Persistence_landscape* > persistence_of_point_cloud_in_dimension_2;
	
	
	//Now generate the point clouds and compute their persistence:
	for ( size_t i = 0 ; i != number_of_samples ; ++i )
	{
		std::cout << "Generating point cloud number : " << i << std::endl;
		
		std::vector< Point > pc1 = generate_random_point_cloud_in_given_dimension( dimension1 , number_of_points_to_sample );
		std::vector< Point > pc2 = generate_random_point_cloud_in_given_dimension( dimension2 , number_of_points_to_sample );
		
		std::cout << "Normalization of the obtained point clouds. \n";
		normalize_distance_between_points( pc1 );
		normalize_distance_between_points( pc2 );
				
		Rips_complex rips1(pc1, threshold, Gudhi::Euclidean_distance());
		Rips_complex rips2(pc2, threshold, Gudhi::Euclidean_distance());
			
		Simplex_tree Rips_st1;
		Simplex_tree Rips_st2;
		
        rips1.create_complex(Rips_st1, 2);        
        rips2.create_complex(Rips_st2, 2);
		
		
		Persistent_cohomology< Simplex_tree, Field_Zp > pcoh1(Rips_st1);				
		Persistent_cohomology< Simplex_tree, Field_Zp > pcoh2(Rips_st2);				
		
		//we compute persistence over Z_2
		pcoh1.init_coefficients(2);
		pcoh2.init_coefficients(2);
		
		pcoh1.compute_persistent_cohomology(0);
		pcoh2.compute_persistent_cohomology(0);
		
		
		std::vector< std::pair< Filtration_value , Filtration_value > > ph1 = pcoh1.intervals_in_dimension(dimension_of_persistence);
		std::vector< std::pair< Filtration_value , Filtration_value > > ph2 = pcoh2.intervals_in_dimension(dimension_of_persistence);
		
		//now construct persistence landscapes:
		Persistence_landscape* l1 = new Persistence_landscape(ph1);
		Persistence_landscape* l2 = new Persistence_landscape(ph2);
		
		persistence_of_point_cloud_in_dimension_1.push_back( l1 );
		persistence_of_point_cloud_in_dimension_2.push_back( l2 );		
	}
	std::cout << "Done with the data generation. \n";
	
	//Now we have two collections of persistence landscapes. We can compute their average:
	
	Persistence_landscape av1;
	av1.compute_average(persistence_of_point_cloud_in_dimension_1);
	
	Persistence_landscape av2;
	av2.compute_average(persistence_of_point_cloud_in_dimension_2);
	
	//now that we have the averages, we can go ahead and compute their distance:
	double distance_of_averages = av1.distance(av2);
	
	std::cout << "Distance between average landscape in dimension " << dimension1 << " and the average landscape in dimension " << dimension2 << " is : " << distance_of_averages << std::endl;

	
	unsigned number_of_times_bootstrap_will_run = 1000;

	std::vector< Persistence_landscape* > all_landscapes;
	all_landscapes.insert(all_landscapes.end(), persistence_of_point_cloud_in_dimension_1.begin(), persistence_of_point_cloud_in_dimension_1.end());
	all_landscapes.insert(all_landscapes.end(), persistence_of_point_cloud_in_dimension_2.begin(), persistence_of_point_cloud_in_dimension_2.end());
	unsigned nnumber_of_cases_local_distance_is_larger_than_global = 0;	
	
	std::cerr << "Progress ";
	for  ( size_t try_no = 0 ; try_no != number_of_times_bootstrap_will_run ; ++try_no )  
	{
		if ( try_no%(number_of_times_bootstrap_will_run/10) == 0 ) std::cerr << ".";
		std::random_shuffle ( all_landscapes.begin(), all_landscapes.end() );
		std::vector< Persistence_landscape* > first_half;
		std::vector< Persistence_landscape* > second_half;
		first_half.reserve( (unsigned)(all_landscapes.size()/2) );
		second_half.reserve( (unsigned)(all_landscapes.size()/2) );
		for ( size_t i = 0 ; i != (unsigned)(all_landscapes.size()/2) ; ++i )
		{
			first_half.push_back( all_landscapes[i] );
			second_half.push_back( all_landscapes[(unsigned)(all_landscapes.size()/2)+i] );
		}		
		
		Persistence_landscape local_av1;
		local_av1.compute_average(first_half);
		
		Persistence_landscape local_av2;
		local_av2.compute_average(second_half);
		
		double local_distance = local_av1.distance(local_av2);	
		
		//std::cout << "local_distance : " << local_distance << std::endl;			
		
		if ( local_distance > distance_of_averages )++nnumber_of_cases_local_distance_is_larger_than_global;			
	}
	
	std::cout << std::endl << "Number of cases out of " << number_of_times_bootstrap_will_run << " in which case we got larger distance between averages that in the initial case : " << nnumber_of_cases_local_distance_is_larger_than_global << std::endl;
	
	for ( size_t i = 0 ; i != all_landscapes.size() ; ++i )
	{
		delete all_landscapes[i];
	}
	

	return 0;
}
